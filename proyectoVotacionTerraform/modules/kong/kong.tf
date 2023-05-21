resource "aws_ecs_cluster" "my_cluster_kong" {
  name = "my-cluster-kong" # Naming the cluster
}

resource "aws_ecs_task_definition" "kong" {
  family                = "${var.app_name_kong}"
  execution_role_arn    = "arn:aws:iam::${var.id_aws}:role/${var.role}"
  network_mode          = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  container_definitions = <<DEFINITION
  [
  {
    "name": "${var.app_name_kong}",
    "container_name": "${var.app_name_kong}",
    "image": "${var.id_aws}.dkr.ecr.${var.region_aws}.amazonaws.com/${var.image_kong}",
    "portMappings": [
      {
        "ContainerPort": ${var.kong_port_http},
        "Protocol"      : "tcp",
        "hostPort": ${var.kong_port_http}
      }
    ],
    "environment": [
      {
         "name"  : "KONG_DATABASE",
         "value" : "off"
      },
      {
         "name"  : "KONG_DECLARATIVE_CONFIG",
         "value" : "/kong.yml"
      }
    ]
  }
]
DEFINITION
cpu                      = "256"
memory                   = "512"
}
# Provide a reference to your default VPC
resource "aws_default_vpc" "default_vpc" {
  enable_dns_hostnames = true
}


resource "aws_default_subnet" "default_subnet_a" {
  # Use your own region here but reference to subnet 1a
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true
}

resource "aws_default_subnet" "default_subnet_b" {
  # Use your own region here but reference to subnet 1b
  availability_zone = "us-east-1b"
  map_public_ip_on_launch = true
}


resource "aws_ecs_service" "kong" {
  name                = "${var.app_name_kong}"
  launch_type         = "FARGATE"
  cluster             = "${aws_ecs_cluster.my_cluster_kong.id}"
  task_definition     = "${aws_ecs_task_definition.kong.arn}"
  desired_count       = 2

  load_balancer {
    target_group_arn  = "${aws_lb_target_group.target_group_kong.arn}"
    container_name    = "${aws_ecs_task_definition.kong.family}"
    container_port    = "${var.kong_port_http}"
    
  }

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_a.id}", "${aws_default_subnet.default_subnet_b.id}"]
    assign_public_ip = true # Providing our containers with public IPs
    security_groups  = ["${var.ecs_service_kong_id}"] # Setting the security group
  }
  depends_on = [aws_alb.application_load_balancer_kong, aws_ecs_task_definition.kong]
}

resource "aws_lb_target_group" "target_group_kong" {
  name        = "target-group-kong"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = "${aws_default_vpc.default_vpc.id}" # Referencing the default VPC
  health_check {
    healthy_threshold = "2"
    unhealthy_threshold = "6"
    interval = "30"
    matcher = "200,301,302"
    path = "/"
    protocol = "HTTP"
    timeout = "20"
  }
}

resource "aws_alb" "application_load_balancer_kong" {
  name               = "kong-balancer" # Naming our load balancer
  load_balancer_type = "application"
  subnets = [ # Referencing the default subnets
    "${aws_default_subnet.default_subnet_a.id}",
    "${aws_default_subnet.default_subnet_b.id}"
  ]
  # Referencing the security group
  security_groups = ["${var.load_balancer_security_group_kong_id}"]
}

resource "aws_lb_listener" "listener_kong" {
  load_balancer_arn = "${aws_alb.application_load_balancer_kong.arn}" # Referencing our load balancer
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = "${aws_lb_target_group.target_group_kong.arn}" # Referencing our tagrte group
  }
}



output "kong_url" {
  value = aws_alb.application_load_balancer_kong.dns_name
}
