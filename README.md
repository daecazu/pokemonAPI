# Django Pokemon service

This service allows to use a command to fetch information from pokemon API, that information is persisted on a database and can be retrive using and endpoint and filtering by name.

## Pokemon fetch Commando

you can use pokemon_fetch commando to retrieve information related to a pokemon chain-evolution, id must be an integer.

`docker-compose -f compose-dev.yml run --rm django sh -c 'python manage.py pokemon_fetch {id}'`


## Local Server commands (DEV)

**Adding Docker-compose File**

**Building project**

`docker-compose -f compose-dev.yml build`

**Running Tests**

`docker-compose -f compose-dev.yml run --rm django sh -c 'python manage.py test && flake8'`

**Create SuperUser**

`docker-compose -f compose-dev.yml run --rm django sh -c 'python manage.py createsuperuser'`

**Run Local Server**

`docker-compose -f compose-dev.yml up`

## Remote Server commands (Production)

**Building project**

`docker-compose -f compose-prod.yml build`

**Create SuperUser**

`docker-compose -f compose-prod.yml run --rm django sh -c 'python manage.py createsuperuser'`

**Run Local Server**

`docker-compose -f compose-prod.yml up -d`

### Create a secret key

in python 3.6 we can use these 3 lines

```python
import secrets
import string 
print("".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)))
```
is best practice to create a secret key for each project in the .envs/production/django file

### Create production env files

create .envs files, in order to work the service needs these files:

- .envs/.production/.django
- .envs/.production/.postgres


#### Django
DJANGO_SECRET_KEY=
DJANGO_SETTINGS_MODULE=

#### PostgreSQL
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
