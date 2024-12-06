
## To the run Application:
>flask --app microblog.py run --debug

the pot file are needed for the translation for the language first a .pot file will
created for the all the languages then they get converted into the specified language.

## To extract all the texts to a .pot file:
>pybabel extract -F babel.cfg -k _l -o messages.pot .

## To create a translation for each language:
>pybabel init -i messages.pot -d app/translations -l hi

for other language just replace the country code for Hindi it is hi and for Spanish it is es

The messages.po file is a sort of source file for translations. When you want to start using these translated texts, this file needs to be compiled into a format that is efficient to be used by the application at run-time. 
## To compile all the translations for the application, you can use following command:
>pybabel compile -d app/translations

## To update translation if some changes made to the templates or add a new template 
which need be to translate. 
>pybabel extract -F babel.cfg -k _l -o messages.pot .
>pybabel update -i messages.pot -d app/translations


These are commands are long and complicated so I create a cli command for them

## To add a new language
>flask translate init <language-code>

## To update all the languages after making changes to the _() and _l() language markers:
>flask translate update

## To compile all languages after updating the translation files:
>flask translate compile

## To test email functionality you can use an emulated email server, you can start second terminal with the following command:
>aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025

or another alternative is to use a dedicated email service such as SendGrid, which allows you to send up to 100 emails per day on a free account.

## To create migration repository to manage database migration:
>flask db init

## If any changes made to the models needs to reflected to the database so
new database migration needs to generated.
> flask db migrate -m "message for commit"

## And the migration needs to be applied to the database:
>flask db upgrade


## To erase the models or want to go back to previous changes made to the database,
use the command:
>flask db downgrade base
>flask db upgrade

## To start Elasticsearch:
install the elasticsearch cd into bin folder then run it as service
for detailed explation see the [documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html#install-windows)
>elasticsearch-service.bat start

## Start Redis to manage redis queue:

RQ does not run on the Windows native Python interpreter. If you are using the Windows platform, you can use wsl or download [docker](https://docs.docker.com/desktop/setup/install/windows-install/) then run redis. Make sure docker is running and then use the
poweshell or cmd to run commands:

## Pull and Run the Redis Docker Image:
>docker pull redis:latest

## Run a Redis Container: Start a Redis container with this command:
>docker run -d --name redis-container -p 6379:6379 redis:latest

## Stop and Start the Redis Container:
>docker start redis-container
>docker stop redis-container