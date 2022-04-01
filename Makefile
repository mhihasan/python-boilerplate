.PHONY: test
test:
	docker-compose run user-service pytest .

.PHONY: install
install:
	pip install -Ur requirements/dev.txt

.PHONY: run_server
run_server:
	docker-compose up --build --force-recreate  --remove-orphans

.PHONY: run_dev
run_dev:
	uvicorn src.main:app --reload
