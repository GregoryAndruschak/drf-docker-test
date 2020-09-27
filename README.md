# drf-docker-test

CRUD API for posts and comments on them. 
Uses Django REST Framework, PostgreSQL, nginx and docker. 

API documentation: https://www.getpostman.com/collections/d09facd66266bdcb092b

## How to build it

### Manual usage:

```
$ docker-compose -f docker-compose.yml down -v
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec web python manage.py makemigrations --noinput
$ docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
```
