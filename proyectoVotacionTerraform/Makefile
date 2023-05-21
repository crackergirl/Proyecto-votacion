all: service-web-db config-kong push-kong service-kong

destroy-all: delete-image-kong-ecr plan 
	terraform destroy

destroy: init plan 
	terraform destroy

plan: init
	terraform plan
	
service-web-db: init
	terraform plan -target=module.my_service
	terraform apply -target=module.my_service

config-kong: init
	terraform plan -target=module.config_kong
	terraform apply -target=module.config_kong

service-kong: init
	terraform plan -target=module.kong
	terraform apply -target=module.kong

delete-image-kong-ecr: init
	terraform plan -target=module.delete_image_kong_ecr
	terraform apply -target=module.delete_image_kong_ecr

init:
	terraform init

##push image Kong - es necesario tener docker arrancado

push-kong:
	docker build -t kong ECRKong/.
	chmod +x ECRKong/pushContainer.sh
	sh ECRKong/pushContainer.sh
	docker image rm  kong:latest
	docker image rm  420113822787.dkr.ecr.us-east-1.amazonaws.com/kong:latest





