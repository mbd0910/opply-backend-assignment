# Local development



## Populating the database with sample data

There's a Django management command in the opply/api app which you can use to populate the database with some sample
data.

```shell
docker-compose exec web python manage.py sample_db
```
