
# image-resizer
Сервис для изменения размера фотографий.

# Getting Started
Для запуска необходимо: 
- установить в виртуальное окружение зависимости из файла requirements.txt:  pip install -r requirements.txt 
- Далее необходимо создать миграции: python manage.py makemigrations
- Выполнить миграции: python manage.py migrate
- Создать администратора: python manage.py createsuperuser

Для запуска на боевом сервере необходимо установить wsgi (к примеру gunicorn) И использовать боевой сервер, например nginx
Изменить настройки проекта таким образом, чтобы секретная информация хранилась в .env например с помощью django-environ
Поставить Debug = False и изменить настройки связанные с раздачей медиа и статических файлов. 

# Built With
Django v3.1.6
Sqlite3

# Versioning
На данный момент версия проекта v1. Чтобы узнать доступные версии смотрите теги в этом репозитории.


# Authors
Balashov Konstantin


# Acknowledgments
Спасибо, всем кто воспользовался данным сервисом, буду рад обратной связи.
