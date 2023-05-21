#configuración cuenta
variable "id_aws" {
  default = "420113822787"
}
variable "region_aws" {
  default = "us-east-1"
}
variable "role" {
  default = "LabRole"
}



#imágenes
variable "image_app" {
  default = "app-repo:latest"
}

variable "image_kong" {
  default = "kong:3.1.1"
}

# Kong
variable "app_name_kong" {
  default = "kong"
}

variable "kong_port_admin" {
  default = 8001
}
variable "kong_port_http" {
  default = 8000
}
variable "kong_port_https" {
  default = 8443
}

variable "container_memory_reservation" {
  default = 64
}

//db

variable "settings" {
  description = "Configuracion settings"
  type = map(any)
  default = {
    "database" = {
      allocated_storage    = 10
      db_name              = "voting_data"
      engine               = "mysql"
      engine_version       = "5.7"
      instance_class       = "db.t3.micro"
      parameter_group_name = "default.mysql5.7"
      skip_final_snapshot  = true
    }

  }

}

variable "db_username" {
  default = "rootrootroot"
}

variable "db_password" {
  default = "rootrootroot"
}
