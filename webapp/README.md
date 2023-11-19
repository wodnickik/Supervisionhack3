Aplikacja używa bazy postgres, wymagany jest plik .env w folderze supervisionhack3/webapp/webapp
w formacie:

SECRET_KEY = "sekcretkey"

db_name = "db_name"
db_user = "db_user"
db_pass = "db_pass"
db_host = "db_host"
db_port = "db_port"

Odpalanie strony:

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Odpalanie frontenu opisane w oddzielnym pliku README w folderze light-bootstrap-dashboard-react-master

