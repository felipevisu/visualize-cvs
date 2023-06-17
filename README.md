# Visualize CVS

Projeto em Python/Django com API Graphql para recebimento de currículos para vagas em empresas.

### Recursos extras
* Deploy no  Heroku
* Envio de notificações com sendgrid

## Execução local

Em um ambiente Linux iniciar e execultar uma numa `venv`
```
virtualenv venv
source venv bin activate
```
Instalar dependências
```
pip install -r requirements.txt
```
Configurar arquivo .env
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
Executar em local host
```
python manage.py runserver
```
