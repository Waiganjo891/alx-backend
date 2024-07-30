0x02. i18n
Flask-Babel is an extension to Flask that adds i18n and l10n support to any Flask application with the help of babel, pytz and speaklater. It has builtin support for date formatting with timezone support as well as a very simple and friendly interface to gettext translations.

0. Basic Flask app
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).

1. Basic Babel setup
Install the Babel Flask extension:
$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.
In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en") and timezone ("UTC").
Use that class as config for your Flask app.
