.PHONY: 

down:
	docker-compose down
volume:
	docker volume prune -f
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
	docker ps -a
init: down volume up
ps:
	docker-compose ps
deploy:
	docker-compose run --rm api sls deploy
test:
	docker-compose run --rm api pytest
