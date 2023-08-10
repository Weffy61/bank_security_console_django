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
В файле `settings.py`, расположенном в директории `project` необходимо прописать свои данные для доступа к БД
```djangourlpath
'ENGINE': 'ENGINE',
'HOST': 'HOST',
'PORT': 'PORT',
'NAME': 'NAME',
'USER': 'USER',
'PASSWORD': 'PASSWORD'
```
## Запуск
```commandline
python main.py
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.