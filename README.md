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
