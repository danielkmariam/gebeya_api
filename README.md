###
Running migration

```
$ python db/manage.py db init
$ python db/manage.py db migrate -m '<text will be used on file name>'
$ python db/manage.py db upgrade
$ python db/manage.py db --help