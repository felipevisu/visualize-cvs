# Visualize CVS

Project build in Python/Django with a Graphql API to receive CVs on jobs applications.

### RExtra resourses
* Deploy on Heroku
* Notification system with SendGrid

## Localhost execution

In an envirounment with Linux start and excecute a python virtualenv `venv`
```
virtualenv venv
source venv bin activate
```
Install the dependencies
```
pip install -r requirements.txt
```
Configure the .env file
```
SECRET_KEY=
DEBUG=
SENDGRID_API_KEY=
DEFAULT_FROM_EMAIL=
DEFAULT_TO_EMAIL=
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
MEDIA_URL=
STATIC_URL=
```
Run in localhost
```
python manage.py runserver
```
