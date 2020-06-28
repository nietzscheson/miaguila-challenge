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
import:
	docker-compose run --rm mongo mongoimport --host mongo --db trips --authenticationDatabase admin --username root --password example --drop --file trips.json --jsonArray
trip:
	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:5000/trips --data  @trip.json
test: init import
	docker-compose run --rm api pytest
