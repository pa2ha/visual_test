# Как запустить проект
Клонировать репозиторий
```
git clone git@github.com:pa2ha/visual_test.git
$ cd visual_test
```
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Находясь рядом с файлом manage.py выполнить миграции и запустить сервер

```
python manage.py migrate
python manage.py runserver
```
# Эндпоинты
Веб сервис будет доступен по адресу - http://127.0.0.1:8000/
Так же доступно API - http://127.0.0.1:8000/api/users/

## Регистрация
Регистрация проходит POST запросом http://127.0.0.1:8000/api/users/
указав в теле запроса имя и почту
```
{
    "name": "TestName1",
    "email": "TestPassword1"
    
}
```
Получить список пользователей можно при помощи GET запроса - http://127.0.0.1:8000/api/users/


Получить конкретного пользователя можно указав в адресе его id, например http://127.0.0.1:8000/api/users/1


Удалить пользователя можно DELETE запросом на его персональный эндпоинт, например http://127.0.0.1:8000/api/users/1
