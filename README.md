# Пульт наблюдения за сотрудниками
Панель для наблюдения за перемещением сотрудников в хранилище.  
При нахождении в хранилище более часа флаг меняется на `True`.  
## Установка
```commandline
git clone https://github.com/Weffy61/bank_security_console_django
```
## Установка зависимостей
Переход в директорию с исполняемым файлом и установка
```commandline
cd bank_security_console_django
```
```commandline
pip install -r requirements.txt
```
## Настройка
В корне проекта необходимо создать файл `.env`. В него внести данные доступа к вашей БД в формате URL. 
[Подробнее](https://github.com/jazzband/dj-database-url#url-schema).  
Пример:  

```djangourlpath
export DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/NAME
``` 
Также по необходимости добавить следующие поля  
```djangourlpath
export SECRET_KEY=SECRET_KEY
export DEBUG=True`
export ALLOWED_HOSTS=[*]
```
## Запуск
```commandline
python manage.py runserver
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.