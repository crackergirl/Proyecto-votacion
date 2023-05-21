resource "aws_security_group" "db_security_group" {
  vpc_id      = "${aws_default_vpc.default_vpc.id}"
  ingress {
    from_port = 3306
    to_port   = 3306
    protocol  = "tcp"
    # Only allowing traffic in from the service security group
    security_groups = ["${aws_security_group.service_security_group.id}"]
  }
}

resource "aws_db_subnet_group" "db_subnet_group"{
  name = "subnet_group_db"
  subnet_ids = ["${aws_default_subnet.default_subnet_a.id}", "${aws_default_subnet.default_subnet_b.id}"]
}

resource "aws_db_instance" "default" {
  allocated_storage    = var.settings.database.allocated_storage
  db_name              = var.settings.database.db_name
  engine               = var.settings.database.engine
  engine_version       = var.settings.database.engine_version
  instance_class       = var.settings.database.instance_class
  username             = var.db_username
  password             = var.db_password
  db_subnet_group_name = aws_db_subnet_group.db_subnet_group.id
  vpc_security_group_ids = [aws_security_group.db_security_group.id]
  skip_final_snapshot  = var.settings.database.skip_final_snapshot
}



