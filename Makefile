.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS := -e -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

CURRENT_CONDA_ENV_NAME = adventofcode2022
ACTIVATE_CONDA = source $$(conda info --base)/etc/profile.d/conda.sh
CONDA_ACTIVATE = $(ACTIVATE_CONDA) ; conda activate ; conda activate $(CURRENT_CONDA_ENV_NAME)

.PHONY: \
test \
run \
mypy \
flake8

YEAR = 2022
DAY = 01_day
CURRENT_DAY = $(YEAR)/$(DAY)
SCRIPT = calories.py

run:
	$(CONDA_ACTIVATE)
	cd $(CURRENT_DAY)
	./$(SCRIPT)

test:
	$(CONDA_ACTIVATE)
	cd $(CURRENT_DAY)
	coverage run -m pytest -xv --capture=no test_$(SCRIPT)
	coverage report -m
	python -m pytest --html=reports.html

lint:
	$(CONDA_ACTIVATE)
	pylint $(CURRENT_DAY)/$(SCRIPT)

mypy:
	$(CONDA_ACTIVATE)
	mypy $(CURRENT_DAY)/$(SCRIPT)
