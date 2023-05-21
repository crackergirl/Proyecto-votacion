#configuración cuenta
variable "id_aws" {
}
variable "region_aws" {
}
variable "role" {
}

#security group kong
variable "ecs_service_kong_id"{
}

#imágenes
variable "image_app" {
  default = "app-repo:latest"
}


variable "container_memory_reservation" {
  default = 64
}

#db
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
      username             = "rootrootroot"
      password             = "rootrootroot"
      parameter_group_name = "default.mysql5.7"
      skip_final_snapshot  = true
    }

  }

}

