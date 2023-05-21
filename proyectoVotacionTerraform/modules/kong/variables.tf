#configuración cuenta
variable "id_aws" {

}
variable "region_aws" {

}
variable "role" {

}

# Kong
variable "image_kong" {
  default = "kong:latest"
}
variable "app_name_kong" {
  default = "kong"
}
variable "kong_port_http" {
  default = 8000
}

variable "load_balancer_security_group_kong_id"{
}
variable "ecs_service_kong_id"{
}


