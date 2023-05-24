terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
  profile = "default"
  shared_credentials_file = "credentials"
}

module "my_service" {
  source = "./modules/servicioWebDB"
  ecs_service_kong_id = "${aws_security_group.ecs_service_kong.id}"
  id_aws = "${var.id_aws}"
  region_aws = "${var.region_aws}"
  role = "${var.role}"

}

module "config_kong" {
  source = "./modules/configKong"
  dns_balanceador_web = module.my_service.app_url
  depends_on = [module.my_service]

}

module "kong" {
  source = "./modules/kong"
  load_balancer_security_group_kong_id = "${aws_security_group.load_balancer_security_group_kong.id}"
  ecs_service_kong_id = "${aws_security_group.ecs_service_kong.id}"
  depends_on = [module.config_kong]
  id_aws = "${var.id_aws}"
  region_aws = "${var.region_aws}"
  role = "${var.role}"
}


module "delete_image_kong_ecr" {
  source = "./modules/deleteImageKong"
  depends_on = [module.config_kong]
}

resource "aws_security_group" "ecs_service_kong" {
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    # Only allowing traffic in from the load balancer security group
    security_groups = ["${aws_security_group.load_balancer_security_group_kong.id}"]
  }

  egress {
    from_port   = 0 # Allowing any incoming port
    to_port     = 0 # Allowing any outgoing port
    protocol    = "-1" # Allowing any outgoing protocol 
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic out to all IP addresses
  }
}

resource "aws_security_group" "load_balancer_security_group_kong" {
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


output "app_url" {
  value = module.my_service.app_url
}

output "kong_url" {
  value = module.kong.kong_url
}

