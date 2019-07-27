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
	@echo To activate virtual environment please run: source ~/r2ml/bin/activate
	@echo To deactive virtual environment enter: deactivate

setup_docker:
ifeq ($(OS_NAME), linux)
	sudo apt install docker-compose
endif
	docker-compose -f docker/docker-my-sql.yml up

setup_database:
ifeq ($(OS_NAME), linux)
	sudo apt install mysql-client
endif
	mysql -h 127.0.0.1 -P 3306 -u root -D mysql-development < python/sql/fillDatabases.sql
