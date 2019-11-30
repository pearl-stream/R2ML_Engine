# R2RML

Create a tool that transforms relational data to RDF based on arbitrary R2RML mappings

## Installation
1. `make setup` Installs all dependecies and creates python3.5 virtual environment
2. `source r2ml/bin/activate` activates virtual environment
3. `make setup_env`

## Usage

Run following commands after installation. Always remember to activate the virtual environment by typing `source r2ml/bin/activate`. 
1. In one terminal start docker with mysql database `make start_docker`
2. In second terminal activate virtualenvironment `source r2ml/bin/activate`
3. If *requirements.txt* changed run `make setup_env` to reproduce the state of your virtual python environment
4. Fill database `make fill_db`
5. **Install new python modules with pip**. If you installed new python modules run `make freeze_env` to update the *requirements.txt*. Then upload the changed file, such that others can reproduce your state of the python environment
6. When finished working run `deactivate` to deactivate virtual python environent

- files in `model` will be added to SQL-DB


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Start Docker with Database
For awesome Mac users (1) and (2) has probably be executed 
```
eval "$(docker-machine env default)"
export COMPOSE_TLS_VERSION=TLSv1_2

docker-compose -f docker-my-sql.yml up
```

## Connect to mysql when docker is running:
```
mysql -h 127.0.0.1 -P 3306 -u root -D mysql-development
```

In case this ip does not work have a look to the IP of the docker container:
```
docker-machine ip
```
## Fill database with sql script
```
mysql -h 127.0.0.1 -P 3306 -u root -D mysql-development < python/sql/fillDatabases.sql 
```
