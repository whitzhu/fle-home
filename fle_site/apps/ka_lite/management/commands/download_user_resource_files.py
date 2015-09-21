import os
import urllib

from django.conf import settings
from django.core.management.base import NoArgsCommand

from ...models import UserResource

class Command(NoArgsCommand):
    help = """Downloads user resource PDFs and puts them in the appropriate location."""

    def handle_noargs(self, **opts):

        user_resource_path = settings.MEDIA_ROOT + "user_resources/"
        if not os.path.exists(user_resource_path):
            os.makedirs(user_resource_path)

        for res in UserResource.objects.all():
            if res.is_google_doc:
                url = res.get_google_download_url()
                path = res.get_download_path()
                path, msg = urllib.urlretrieve(url, path)
                self.stdout.write("Downloaded %s to %s\n\n" % (url, path))
