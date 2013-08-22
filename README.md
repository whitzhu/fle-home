# FLE Site 

Starting from the ground up with the new FLE site to _make_ _things_ _work_

## Environment Setup 

First, install [pip](https://pypi.python.org/pypi/pip) if you don't have it already. 

If you don't have [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) installed, install it with:

`pip install virtualenvwrapper`

Next, clone the repo:

`git clone git@github.com:dylanjbarth/fle_redesign.git`

Now, make a virtualenvwrapper to install dependencies:

`mkvirtualenv fle_site`

Install dependencies:

`pip install django==1.4.3`
`pip install South==0.8.2`
`pip install radpress==0.4.1`
`pip install PIL==1.1.7

Set up the database:

`python manage.py syncdb --migrate`

Run the server:

`python manage.py runserver`

Boom!

## Directory Structure

├── LICENSE
├── README.md
├── fle_redesign
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── apps
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   └── main
│   │       ├── __init__.py
│   │       ├── __init__.pyc
│   │       ├── migrations
│   │       │   ├── 0001_initial.py
│   │       │   ├── 0001_initial.pyc
│   │       │   ├── __init__.py
│   │       │   └── __init__.pyc
│   │       ├── models.py
│   │       ├── models.pyc
│   │       ├── tests.py
│   │       ├── views.py
│   │       └── views.pyc
│   ├── database.sqlite
│   ├── libs
│   │   └── __init__.py
│   ├── local_settings.py
│   ├── local_settings.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── static
│   │   ├── bootstrap
│   │   │   ├── css
│   │   │   │   ├── bootstrap-responsive.css
│   │   │   │   ├── bootstrap-responsive.min.css
│   │   │   │   ├── bootstrap.css
│   │   │   │   └── bootstrap.min.css
│   │   │   ├── img
│   │   │   │   ├── glyphicons-halflings-white.png
│   │   │   │   └── glyphicons-halflings.png
│   │   │   └── js
│   │   │       ├── bootstrap.js
│   │   │       └── bootstrap.min.js
│   │   ├── css
│   │   │   ├── base.less
│   │   │   └── landingpage.less
│   │   ├── img
│   │   │   ├── KA_Lite-vertical-logo.png
│   │   │   ├── content-container.png
│   │   │   ├── fle-logo.jpg
│   │   │   ├── fle-prov-logo-small.png
│   │   │   ├── fle-text-horiz.png
│   │   │   ├── header.png
│   │   │   ├── horizontal-logo-small.png
│   │   │   ├── ka-black-white.png
│   │   │   ├── main-featured.png
│   │   │   ├── purple.png
│   │   │   └── subtle_white_feathers.png
│   │   └── js
│   │       └── less.js
│   ├── templates
│   │   ├── base.html
│   │   └── home.html
│   ├── urls.py
│   ├── urls.pyc
│   ├── wsgi.py
│   └── wsgi.pyc
├── manage.py
└── requirements.txt

