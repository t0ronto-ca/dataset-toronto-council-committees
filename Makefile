setup:
	pip install --quiet -r scripts/requirements-test.txt

validate: setup ## Validate data
	python scripts/validate_yaml.py

json: setup ## Generate JSON from YAML
	python scripts/yaml2json.py < data/committees.yml > outputs/committees.json

dummy: ## Perform a dummy action with outputs
	python scripts/run_dummy_action.py

%:
	@true

.PHONY: help

help:
	@echo 'Usage: make <command>'
	@echo
	@echo 'where <command> is one of the following:'
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
