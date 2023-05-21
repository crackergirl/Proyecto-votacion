resource "null_resource" "force_delete_repository" {
  provisioner "local-exec" {
    command = <<-EOT
      aws ecr batch-delete-image --repository-name kong --image-ids imageTag=latest
    EOT
  }
}

