import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
try:
	site.addsitedir('/home/ubuntu/.virtualenvs/fle-site/local/lib/python2.7/site-packages/')
except:
	pass

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

# Add the app's directory to the PYTHONPATH
sys.path.append(os.path.join(PROJECT_PATH, ".."))
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, "apps")

os.environ["DJANGO_SETTINGS_MODULE"] = "fle_site.settings"

# Activate your virtual env
try:
	activate_env=os.path.expanduser("/home/ubuntu/.virtualenvs/fle-site/bin/activate_this.py")
	execfile(activate_env, dict(__file__=activate_env))
except:
	pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
