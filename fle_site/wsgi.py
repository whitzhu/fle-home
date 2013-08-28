import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
try:
	site.addsitedir('/home/ubuntu/.virtualenvs/fle-site/local/lib/python2.7/site-packages/')
except:
	pass

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/ubuntu/fle-site')
sys.path.append('/home/ubuntu/fle-site/fle_site')
sys.path.append('/home/ubuntu/fle-site/fle_site/apps')

os.environ["DJANGO_SETTINGS_MODULE"] = "fle_site.settings"

# Activate your virtual env
try:
	activate_env=os.path.expanduser("/home/ubuntu/.virtualenvs/fle-site/bin/activate_this.py")
	execfile(activate_env, dict(__file__=activate_env))
except:
	pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
