# Curriculum Vitae

**This is the source code of my personal résumé, published at
  https://jaapjoris.nl/. It is a simple
  [Django](https://www.djangoproject.com/) project that uses
  [SimpleCMS](https://github.com/rtts/django-simplecms/) to make it
  editable on the go.**

## Installation

Run the following commands:

    $ pip install -r requirements.txt
    $ ./manage.py migrate
    $ ./manage.py createsuperuser
    $ ./manage runserver

## Usage

Visit http://localhost:8000/edit to add sections to the homepage.

If you're using this to write your own CV, you'll want to at least
change the [base
template](https://github.com/rtts/jaapjoris/blob/main/jaapjoris/templates/base.html).
