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
import:
	docker-compose run --rm mongo mongoimport --host mongo --db trips --authenticationDatabase admin --username root --password example --drop --file trips.json --jsonArray
