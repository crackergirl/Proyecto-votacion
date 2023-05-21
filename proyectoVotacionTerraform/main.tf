resource "aws_ecs_cluster" "my_cluster" {
  name = "my-cluster" # Naming the cluster
}

resource "aws_ecs_task_definition" "definition" {
  family                   = "task_app"
  container_definitions    = <<DEFINITION
  [
    {
      "name": "task_app",
      "container_name": "task_app",
      "image": "${var.id_aws}.dkr.ecr.${var.region_aws}.amazonaws.com/${var.image_app}",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 5000,
          "hostPort": 5000
        }
      ],
      "environment": [
      {
         "name"  : "URL_DATABASE",
         "value" : "${aws_db_instance.default.id}.cx2usmurvpbu.us-east-1.rds.amazonaws.com"
      },
      {
         "name"  : "NAME_DATABASE",
         "value" : "${aws_db_instance.default.db_name}"
      },
      {
         "name"  : "USER",
         "value" : "${aws_db_instance.default.username}"
      },
      {
         "name"  : "PASSWORD",
         "value" : "${aws_db_instance.default.password}"
      }
      ],
      "memory": 512,
      "cpu": 256
    }
  ]
  DEFINITION
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = "arn:aws:iam::${var.id_aws}:role/${var.role}"
  depends_on = [aws_db_instance.default]
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

resource "aws_ecs_service" "my_first_service" {
  name            = "my-first-service"                             # Naming our first service
  cluster         = "${aws_ecs_cluster.my_cluster.id}"             # Referencing our created Cluster
  task_definition = "${aws_ecs_task_definition.definition.arn}" # Referencing the task our service will spin up
  launch_type     = "FARGATE"
  desired_count   = 2 # Setting the number of containers we want deployed to 2

  load_balancer {
    target_group_arn = "${aws_lb_target_group.target_group.arn}" # Referencing our target group
    container_name   = "${aws_ecs_task_definition.definition.family}"
    container_port   = 5000 # Specifying the container port
  }

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_a.id}", "${aws_default_subnet.default_subnet_b.id}"]
    assign_public_ip = true # Providing our containers with public IPs
    security_groups  = ["${aws_security_group.service_security_group.id}"] # Setting the security group
  }

  depends_on = [aws_db_instance.default]

  
}

resource "aws_security_group" "service_security_group" {
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    # Only allowing traffic in from the load balancer security group
    security_groups = ["${aws_security_group.load_balancer_security_group.id}"]
  }

  egress {
    from_port   = 0 # Allowing any incoming port
    to_port     = 0 # Allowing any outgoing port
    protocol    = "-1" # Allowing any outgoing protocol 
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic out to all IP addresses
  }
}

resource "aws_alb" "application_load_balancer" {
  name               = "test-balancer" # Naming our load balancer
  load_balancer_type = "application"
  subnets = [ # Referencing the default subnets
    "${aws_default_subnet.default_subnet_a.id}",
    "${aws_default_subnet.default_subnet_b.id}"
  ]
  # Referencing the security group
  security_groups = ["${aws_security_group.load_balancer_security_group.id}"]
}

# Creating a security group for the load balancer:
resource "aws_security_group" "load_balancer_security_group" {
  ingress {
    from_port   = 80 # Allowing traffic in from port 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic in from all sources
  }

  egress {
    from_port   = 0 # Allowing any incoming port
    to_port     = 0 # Allowing any outgoing port
    protocol    = "-1" # Allowing any outgoing protocol 
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic out to all IP addresses
  }
}

resource "aws_lb_target_group" "target_group" {
  name        = "target-group"
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

resource "aws_lb_listener" "listener" {
  load_balancer_arn = "${aws_alb.application_load_balancer.arn}" # Referencing our load balancer
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = "${aws_lb_target_group.target_group.arn}" # Referencing our tagrte group
  }
}

output "app_url" {
  value = aws_alb.application_load_balancer.dns_name
}

