# FLE Site 

[http://learningequality.org](http://learningequality.org)

## Environment Setup 

These steps should get you up and running in no time! 

First, follow the link and [install pip](https://pypi.python.org/pypi/pip) if you don't have it already. 

Next install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/):
`pip install virtualenvwrapper`

Next, clone the repo:
`git clone git@github.com:learningequality/fle-site.git`

Move into the directory:
`cd <dir_name>`

Now, make a virtualenvwrapper to install dependencies:
`mkvirtualenv <desired_virtualenv_name>`
*Linux users, see the footnote below if you have trouble creating a virtualenv with the mkvirtualenv command

Install the dependencies listed in requirements.txt:
`pip install -r requirements.txt`

Create a local_settings.py file adjacent to the settings.py file. Inside, set DEBUG = True (so static files will load in dev mode): 
`DEBUG = True`

Set up the database:
`python manage.py syncdb --migrate`

Run the server:
`python manage.py runserver`

Boom!

When you're done, you can cancel the virutalenv just use the command
`deactivate`

* Linux users: To get the mkvirtualenv command to work, you may have to add:
source /usr/local/bin/virtualenvwrapper.sh
to your .bashrc file (and restart bash)

You may also have to run: 
sudo apt-get install python-dev
in order to be able to use pip (inside the virtualenv) to install PIL.

## Map disclaimer
The map requires certain data files to use, and you will get an error if you try and view it at /map/ because they haven't been included in the repo. 

## Blog
To view the blog, visit /blog/. To add posts and get a feel for what it might look like, visit /admin/ and create an article. Some features don't seem to be working very well, and it's easy to break it, but it's a start!

