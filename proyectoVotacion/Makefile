all: stop-docker clean-docker
	
stop-docker:

	docker stop $(shell docker ps -q)

clean-docker:

	docker rm $(shell docker ps -a -q)

clean-images:

	docker image rm  $(shell docker images -a -q)

clean-volume:

	docker volume rm $(shell docker volume ls -q)
