# AKRE System (real estate management)

## Initial setup (only for informational purposes)

After setting up the basic folder structure (root-level files, deployments and requiments.txt), I had to run the following commands to setup the django app:
```
docker-compose -f deployments/docker-compose.yml run api django-admin startproject website .
docker-compose -f deployments/docker-compose.yml run api python manage.py startapp {microservice, such as api or calculations}
```

To migrate the initial models, the ones that already come built into the Django framework, using SQLite:
```
docker-compose -f deployments/docker-compose.yml run api python manage.py migrate
```

And to create a super user to have access to Django's admin interface:
```
docker-compose -f deployments/docker-compose.yml run api python manage.py createsuperuser
```

## Terminal commands

To run Makefile, you need to have the make command installed:

```
sudo apt-get install build-essential
```

Then simply run `make install` to initialize the environment (only necessary the first time you're running the app, or after installation requirements change).

To restart the app, run `make restart`.

To view logs, such as error messages, run `make logs`.

To run migration scripts, simply run `make migrate`.

To run automated testes, run the command `make tests`.

## Endpoints

Access http://localhost:5080/admin/ to log into the admin console.

All CRUD API endpoint are mapped to http://localhost:5080/api/ while the calculations are done in a different API http://localhost:5080/calculations/

Postman is recommended for API testing.

## TODO next

- Unit tests for all calculations (priority)
- Authentication
- Query search parameters for all entities
