OS_NAME := $(shell uname -s | tr A-Z a-z)

setup:
ifeq ($(OS_NAME),linux)
	sudo apt install virtualenv
	sudo apt install python3.5
	sudo apt install docker
	sudo apt install docker-compose
	sudo apt install mysql-client
else
	brew install pyenv-virtualenv
	brew install python3.5
	brew install docker 
	brew install docker-compose
	brew install mysql-client
endif

	virtualenv r2ml -p python3.5
	@echo
	@echo
	@echo To activate virtual environment please run: source r2ml/bin/activate
	@echo To deactive virtual environment enter: deactivate
	@echo After activating the environment run \'make setup_env\' to install necessary python libs

setup_env:
ifneq (,$(findstring r2ml,$(VIRTUAL_ENV)))
	pip install -r requirements.txt
else
	@echo Virtual environment is not activated. Please activate the virtual environment!
endif

freeze_env:
ifneq (,$(findstring r2ml,$(VIRTUAL_ENV)))
	pip freeze -l > requirements.txt
else
	@echo Virtual environment is not activated. Please activate the virtual environment!
endif

start_docker:
	docker-compose -f docker/docker-my-sql.yml up
	@echo
	@echo
	@echo To setup database run in another terminal: make fill_db

fill_db:
	mysql -h 127.0.0.1 -P 3306 -u root -D mysql-development < python/sql/fillDatabases.sql
