#!/bin/sh
ACCOUNT_ID="420113822787"
AWS_DEFAULT_REGION="us-east-1"
IMAGE_DOCKER_NAME="prueba"
IMAGE_REPO_NAME="app-repo"
REPOSITORY_URI="$ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
aws ecr get-login-password --region $AWS_DEFAULT_REGION --profile "default" | docker login --username AWS --password-stdin $REPOSITORY_URI 
docker tag $IMAGE_DOCKER_NAME:latest $REPOSITORY_URI/$IMAGE_REPO_NAME:latest
docker push $REPOSITORY_URI/$IMAGE_REPO_NAME:latest