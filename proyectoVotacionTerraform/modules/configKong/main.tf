variable "dns_balanceador_web" {
  description = "dns balanceador variable"
}
resource "local_file" "example" {
  filename = "ECRKong/kong.yml"
  content  = <<EOF
_format_version: "3.0"
_transform: true
services:
- name: my-api-server
  url: http://${var.dns_balanceador_web}:80/
  routes:
  - name: my-api-server
    paths: 
      - /
- name: reset-apikey
  url: http://${var.dns_balanceador_web}:80/api/v1/reset
  routes:
  - name: reset-apikey
    paths:
      - /api/v1/reset
  plugins:
    - name: key-auth
- name: drop-apikey
  url: http://${var.dns_balanceador_web}:80/api/v1/drop
  routes:
  - name: drop-apikey
    paths:
      - /api/v1/drop
  plugins:
    - name: key-auth

- name: new-apikey
  url: http://${var.dns_balanceador_web}:80/api/v1/new
  routes:
  - name: new-apikey
    paths:
      - /api/v1/new
  plugins:
    - name: key-auth

consumers:
- username: my-user
  keyauth_credentials:
  - key: apikey

plugins:
- name: file-log
  config: 
    path: /tmp/file.log
EOF
  
}

resource "aws_ecr_repository" "kong" {
  name = "kong"
  lifecycle {
    prevent_destroy = false
  }
}
