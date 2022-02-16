gendiff:
	poetry run gendiff

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

install:
	poetry install

test:
	poetry run pytest  # --cov=gendiff tests/ --cov-report xml

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: gendiff install test lint selfcheck check build
