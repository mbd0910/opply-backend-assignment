# Local development

## Populating the database with sample data

There's a Django management command in the opply/api app which you can use to populate the database with some sample
data.

```shell
docker-compose exec web python manage.py sample_db
```

# Future improvements

* Replace SQLLite with Postgres. SQLLite is ideal for small projects like this, but for a larger project you'd want 
your database to match whatever you're using in production.
* Automated test suite for API.

## Security

Note: The token authentication provided by Django REST framework is a fairly simple implementation.

For an implementation which allows more than one token per user, has some tighter security implementation details, and supports token expiry, please see the Django REST Knox third party package.

