OS_NAME := $(shell uname -s | tr A-Z a-z)

setup_py:
ifeq ($(OS_NAME),linux)
	sudo apt install virtualenv
	sudo apt install python3.5
else
	brew install pyenv-virtualenv
	brew install python3.5
endif

	virtualenv r2ml -p python3.5
	@echo
	@echo
	@echo To activate virtual environment please run: source r2ml/bin/activate
	@echo To deactive virtual environment enter: deactivate
	@echo After activating the environment run \'make setup_env\' to install necessary python libs

setup_env:
	pip install -r requirements.txt

freeze_env:
	pip freeze -l > requirements.txt

setup_docker:
ifeq ($(OS_NAME), linux)
	sudo apt install docker
	sudo apt install docker-compose
else
	brew install docker 
	brew install docker-compose
endif
	docker-compose -f docker/docker-my-sql.yml up
	@echo
	@echo
	@echo To setup database run in another terminal: make setup_database

setup_database:
ifeq ($(OS_NAME), linux)
	sudo apt install mysql-client
else
	brew install mysql-client
endif
	mysql -h 127.0.0.1 -P 3306 -u root -D mysql-development < python/sql/fillDatabases.sql
