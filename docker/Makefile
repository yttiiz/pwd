COMPOSE=docker compose
API_CONTAINER=pwd
PROJECT_NAME=database-pwd
BAKE=COMPOSE_BAKE=true # Use once with 'up' command

up:
	$(BAKE) $(COMPOSE) --env-file ../.env -p $(PROJECT_NAME) up -d

rmi:
	$(COMPOSE) -p $(PROJECT_NAME) down --rmi local

sh:
	docker exec -it $(API_CONTAINER) sh
