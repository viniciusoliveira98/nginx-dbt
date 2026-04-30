
AIRFLOW_IMAGE_NAME = essential_airflow
AIRFLOW_IMAGE_TAG = 1.0

EMBULK_IMAGE_NAME = essential_embulk
EMBULK_IMAGE_TAG = 1.0


AIRFLOW_DOCKERFILE_PATH = /opt/lakehouse/infra/docker/airflow/Dockerfile
AIRFLOW_COMPOSE_PATH = docker/airflow/docker-compose.yml

EMBULK_DOCKERFILE_PATH = /opt/lakehouse/infra/docker/embulk/Dockerfile
EMBULK_COMPOSE_PATH = docker/embulk/docker-compose.yml

SERVICES_COMPOSE_PATH = /opt/lakehouse/infra/docker/services/docker-compose.yml

AIRFLOW_CONTEXT_DIR = /opt/lakehouse/infra/docker/airflow
EMBULK_CONTEXT_DIR = /opt/lakehouse/infra/docker/embulk

### BUILDS ###
build-airflow:
	docker build -t $(AIRFLOW_IMAGE_NAME):$(AIRFLOW_IMAGE_TAG) -f $(AIRFLOW_DOCKERFILE_PATH) $(AIRFLOW_CONTEXT_DIR)

build-embulk:
	docker build -t $(EMBULK_IMAGE_NAME):$(EMBULK_IMAGE_TAG) -f $(EMBULK_DOCKERFILE_PATH) $(EMBULK_CONTEXT_DIR)

build: build-airflow build-embulk

### COMPOSES ###
compose-up-airflow:
	docker compose -f $(AIRFLOW_COMPOSE_PATH) up -d

compose-up-embulk:
	docker compose -f $(EMBULK_COMPOSE_PATH) up -d

compose-up-services:
	docker compose -f $(SERVICES_COMPOSE_PATH) up -d

compose-up: compose-up-airflow compose-up-embulk compose-up-services

push-airflow:
	docker push $(AIRFLOW_IMAGE_NAME):$(AIRFLOW_IMAGE_TAG)

push-embulk:
	docker push $(EMBULK_IMAGE_NAME):$(EMBULK_IMAGE_TAG)

push: push-airflow push-embulk


clean:
	docker image prune -f

.PHONY: build build-airflow build-embulk compose-up compose-up-airflow compose-up-embulk compose-up-services push push-airflow push-embulk clean
