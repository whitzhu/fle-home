# FLE Site 

Starting from the ground up with the new FLE site to _make_ _things_ _work_. 

## Environment Setup 

These steps should get you up and running! Any issues, please ping me :grin:

First, follow the link and [install pip](https://pypi.python.org/pypi/pip) if you don't have it already. 

Next install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/):
`pip install virtualenvwrapper`

Next, clone the repo:
`git clone git@github.com:dylanjbarth/fle_redesign.git`

Move into the directory:
`cd fle_redesign`

Now, make a virtualenvwrapper to install dependencies:
`mkvirtualenv fle_redesign`

Install the dependencies listed in requirements.txt by copy and pasting the following list into the terminal (you can do it all at once!):
`pip install Django==1.4.3;`
`pip install PIL==1.1.7;`
`pip install Pygments==1.6;`
`pip install South==0.8.2;`
`pip install django-extensions==1.1.1;`
`pip install docutils==0.11;`
`pip install easy-thumbnails==1.3;`
`pip install pygeoip==0.2.7;`
`pip install radpress==0.4.1;`
`pip install six==1.3.0;`
`pip install wsgiref==0.1.2;`

Set up the database:
`python manage.py syncdb --migrate`

Run the server:
`python manage.py runserver`

Boom!

When you're done, you can cancel the virutalenv just use the command
`deactivate`

## Map disclaimer
The map requires certain data files to use, and you will get an error if you try and view it at /map/ because they haven't been included in the repo. 

## Blog
To view the blog, visit /blog/. To add posts and get a feel for what it might look like, visit /admin/ and create an article. Some features don't seem to be working very well, and it's easy to break it, but it's a start!

