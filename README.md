# workgent_backend

Working directory for workgent backend

## Documentation available in form of:

### 1. swagger

    Open url: http://localhost:8000/swagger/

### 2. redoc

    Open url: http://localhost:8000/redoc/

## How to run

0. Create a virtual environment and activate it
1. After pulling the master branch, `npm install requirements.txt`
2. Start a `mysql` server on your local machine
3. Change/modify database settings in `settings.py`
4. Change or modify SMTP settings for email in `settings.py`
5. `manage.py makemigrations && manage.py migrate`
6. manage.py `runserver`

# API for ASSIGNMENT available on:

http://localhost:8000/jobs/
