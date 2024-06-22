# Opply Backend Assignment

Django REST API supporting session and token based authentication, product inventory browsing, user order history and 
order placement.

## Running locally

Build and run the Docker container

```shell
docker-compose up --build
```

In another terminal, run the migrations

```shell
docker-compose exec web python manage.py migrate
```

A Django management command has been included to populate the database with sample data.

```shell
docker-compose exec web python manage.py sample_db
```



## Next steps/future improvements

* Automated test suite for the API. I ran out of time to add this so relied on manual testing. The most useful tests 
would've been for Order creation: 
  * to check that orders were rejected if stock levels were too low
  * to check that stock levels were correctly modified after accepting orders
* Transaction handling should be considered for stock level management to ensure all database changes succeed or none 
do.
* Concurrent updates would need to be handled before horizontally scaling this API. At present, there would be issues 
with inventory stock management if concurrent requests for the same ingredient hit different instances of the API: both
orders may be accepted despite it only being possible for one order to be fulfilled if stock levels are low.
* Replace SQLite with Postgres. SQLite is ideal for small projects like this, but for a larger project you'd want 
your database to match whatever you're using in production.
* According to the docs, the token authentication provided by Django REST framework is a fairly simple implementation.
For improved security (including token expiry), a third party package such as Django REST Knox could be used.
* A shared Postman collection would be a convenient way of sharing example endpoint calls between team members.

## Deployment



## Third party docs/links

* [Assignment brief](https://gist.github.com/martinOpply/c0b496ae1c52ec24899b58bea6b4708d)
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Django REST Knox](https://github.com/jazzband/django-rest-knox)
* [Collaborating in Postman](https://learning.postman.com/docs/collaborating-in-postman/collaborate-in-postman-overview/)
