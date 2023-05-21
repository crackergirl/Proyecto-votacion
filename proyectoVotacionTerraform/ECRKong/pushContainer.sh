#!/bin/sh
ACCOUNT_ID="420113822787"
AWS_DEFAULT_REGION="us-east-1"
IMAGE_DOCKER_NAME="kong"
IMAGE_REPO_NAME="kong"
VERSION="latest"
REPOSITORY_URI="$ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
aws ecr get-login-password --region $AWS_DEFAULT_REGION --profile "default" | docker login --username AWS --password-stdin $REPOSITORY_URI 
docker tag $IMAGE_DOCKER_NAME:$VERSION $REPOSITORY_URI/$IMAGE_REPO_NAME:$VERSION
docker push $REPOSITORY_URI/$IMAGE_REPO_NAME:$VERSION