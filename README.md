## 📖 Установка
Notification-service для начала нужно перейти в локальную директорию компьютера и ввести данные команды:

```
$ git clone https://gitlab.com/ton1k0/notification-service.git
$ cd notification-service
```

### Pip

```
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source .venv/bin/activate
Изменить psycopg2 на psycopg2-binary в файле requirements.txt

(.venv) $ pip install -r requirements.txt
Открыть 1 терминал и ввести эту команду:
(.venv) $ celery -A notification-service worker --loglevel=info
Открыть 2 терминал и ввести эту команду:
(.venv) $ python manage.py runserver
```

### DATABASES

Чтобы использовать базу данных которая находится на онлайн хостинге введите данные из database.txt в нужные поля в файле `django_project/settings.py`:

```python
# django_project/settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres", # in the file database.txt
        "USER": "postgres", # in the file database.txt
        "PASSWORD": "postgres", # in the file database.txt
        "HOST": "db",  # in the file database.txt
        "PORT": 5432,  # in the file database.txt
    }
}
```
### OpenAPI
```python
#api urls
'http://127.0.0.1:8000/client/add-new-client/' # Добавить клиента
# Method 'POST' тело запроса:
{
  "phone_number": int,
  "mobile_operator_code": int,
  "tag": "string",
  "timezone": "string"
}

'http://127.0.0.1:8000/client/<int:pk>/update/' # Изменить данные о клиенте 'PUT'
# Method 'PUT' тело запроса в ссылке указать id Клиента которого надо изменить:
{
  "phone_number": int,
  "mobile_operator_code": int,
  "tag": "string",
  "timezone": "string"
}

'http://127.0.0.1:8000/client/<int:pk>/delete/' # Удалить клиента 
# Method 'DELETE' в ссылке указать id Клиента которого надо удалить


'http://127.0.0.1:8000/mailing/create/' # Создать рассылку 'POST'
# Method 'POST' тело запроса:
{
  "start_datetime": "2023-05-26T00:00:00",
  "end_datetime": "2023-05-26T23:59:59",
  "mobile_operator_code": int,
  "tag": "string",
  "message_text": "string"
}

'http://127.0.0.1:8000/mailing/<int:pk>/update/' # Изменить данные рассылки
# Method 'PUT' тело запроса в ссылке указать id Рассылки которую надо изменить:
{
  "start_datetime": "2023-05-26T00:00:00",
  "end_datetime": "2023-05-26T23:59:59",
  "mobile_operator_code": int,
  "tag": "string",
  "message_text": "string"
}

'http://127.0.0.1:8000/mailing/<int:pk>/delete/' # Удалить рассылку
# Method 'DELETE' в ссылке указать id Рассылки которую надо удалить

'http://127.0.0.1:8000/mailing/statistics/' # Получения общей статистики по 
# созданным рассылкам
# Method 'GET' тело запроса отсутствует

'http://127.0.0.1:8000/mailing/<int:pk>/detail-statistics/' # Получения детальной 
# статистики отправленных сообщений по конкретной рассылке
# Method 'GET' в ссылке указать id Рассылки статиску которой хотим получить

```