gendiff:
	poetry run gendiff

install:
	poetry install

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
