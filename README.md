**Запуск проекта:**

Клон проекта

    git clone https://github.com/TELIDAS/social_media.git

Создание виртуальной среды 

    python -m venv venv

Активация виртуальной среды

    source venv/bin/activate

Установка всех зависимостей 

    pip isntall -r requirements.txt

Миграции в базу данных 

    python manage.py makemigrations

    python manage.py migrate

Локальный запуск проекта

    python manage.py runserver


**DOCKER**

Создание образа

    docker build -r social-media .

Запуск докер контейнера и создание его тэга

    docker run-t social_media .

    docker-compose up -d 
