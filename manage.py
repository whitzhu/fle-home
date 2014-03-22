#!/usr/bin/env python
import glob
import os
import sys

def setup():
    """Fake command for setting up fle_site"""
    from django.core.management import call_command
    PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), "fle_site"))

    print "Setting up static files..."
    call_command('collectstatic', interactive=False)

    print "Setting up database..."
    call_command('syncdb', migrate=True)

    print "Setting up fixtures..."
    fixtures = glob.glob(os.path.join(PROJECT_PATH, 'apps/*/fixtures/*.json'))
    call_command('loaddata', *fixtures)

    print "Setting up local_settings.py..."
    local_settings_filepath = os.path.join(PROJECT_PATH, "local_settings.py")
    if not os.path.exists(local_settings_filepath):
        with open(local_settings_filepath, "a") as fp:
            fp.write("\nDEBUG = True\n")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fle_site.settings")

    from django.core.management import execute_from_command_line

    if "setup" in sys.argv:
        setup()
    else:
        execute_from_command_line(sys.argv)
