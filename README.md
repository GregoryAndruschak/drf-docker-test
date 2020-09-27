# drf-docker-test

CRUD API for posts and comments on them. 
Uses Django REST Framework, PostgreSQL, nginx and docker. 

Postman collection: https://www.getpostman.com/collections/d09facd66266bdcb092b
Postman documentation: https://web.postman.co/collections/12881119-60a6bcc0-e06e-4d3e-a8b6-134104a5801f?version=latest&workspace=cde707cc-8ee1-4b6b-8934-14464c27db6b
Heroku URL: https://drfdockertest.herokuapp.com/

## How to build it

### Manual usage:

```
$ docker-compose -f docker-compose.yml down -v
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec web python manage.py makemigrations --noinput
$ docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
```
