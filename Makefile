OS_NAME := $(shell uname -s | tr A-Z a-z)
IP=127.0.0.1
MACHINE := $$(docker-machine env default)

setup:
ifeq ($(OS_NAME),linux)
	sudo apt install virtualenv
	sudo apt install python3.5
	sudo apt install docker
	sudo apt install docker-compose
	sudo apt install mysql-client
else
	brew install pyenv-virtualenv
	$(eval export LDFLAGS="${LDFLAGS} -L /usr/local/opt/zlib/lib")
	$(eval export CPPFLAGS="${CPPFLAGS} -I /usr/local/opt/zlib/include")
	$(eval export PKG_CONFIG_PATH="/usr/local/opt/zlib/lib/pkgconfig")
	
	brew install zlib
	pyenv install 3.5.0
	brew install docker 
	brew install docker-compose
	brew install mysql-client
	pip3 install virtualenv
	virtualenv -p python3 ~/r2ml
endif
	#pyenv virtualenv r2ml -p 3.5
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
ifeq ($(OS_NAME),darwin)
	$(eval ${MACHINE})
	echo export COMPOSE_TLS_VERSION=TLSv1_2
endif
	docker-compose -f docker/docker-my-sql.yml up
	@echo
	@echo
	@echo To setup database run in another terminal: make fill_db

fill_db:
	mysql -h $(IP) -P 3306 -u root -D mysql-development < python/sql/fillDatabases.sql

