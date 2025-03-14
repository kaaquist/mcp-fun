# MCP Server and MCP Client
There are two servers and one client.


## MySQL Docker Compose
To get a MySQL database use the provided docker-compose.yaml file.
To run it:
```
docker-compose up -d
```
Should then start the container in detached mode - `-d`
```
> docker-compose up
Starting backend_mysql_1 ... done
>
```
Please see the `docker-compose.yaml` for database, user and password.


## MySQL MCP Server
Create a `.env` file with that database, user, password, host and port.
```
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=testuser
MYSQL_PASSWORD=password
MYSQL_DATABASE=testdatabase
``` 
start the server withy the following command
```
uv run --env-file=.env main.py 
```

## MCP Client
Run the following command to start the `client`. Beaware that it can't start if you do not start the MySQL server first
```
uv run --env-file=.env main.py
```

