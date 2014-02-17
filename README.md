# FLE Site 

This is the code for the Foundation for Learning Equality's homepage: [http://learningequality.org](http://learningequality.org)

## Environment Setup 

1. Install requirements: 
    - [install pip](https://pypi.python.org/pypi/pip) if you don't have it already. 
    - install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/): `pip install virtualenvwrapper`

2. Get the codebase: `git clone git@github.com:learningequality/fle-site.git`

3. Make a virtualenv to install dependencies: 
    - `cd <dir_name>`
    - `mkvirtualenv <desired_virtualenv_name>`
    - *Linux users: To get the mkvirtualenv command to work, you may have to add: `source /usr/local/bin/virtualenvwrapper.sh` to your .bashrc file (and restart bash). You may also have to run: `sudo apt-get install python-dev` in order to be able to use pip inside the virtualenv. 
 
4. Install the dependencies listed in requirements.txt: `pip install -r requirements.txt`

5. Create a local_settings.py file as a sibling to the settings.py file. Inside, set `DEBUG = True` (so static files will load in dev mode).

6. Set up the database: `python manage.py syncdb --migrate`

7. Run the server: `python manage.py runserver`

When you're done, you can cancel the virutalenv with the command: 
`deactivate`

## Map disclaimer (localhost:8000/map/)
The map requires certain data files to use, and you will get an error if you try and view it at /map/ because they haven't been included in the repo. 

## Blog
The blog won't work until you add at least one post to it. 


## Issues & style guide
Check out the Issues page for known issues. Use the Wiki for style guide references. 

