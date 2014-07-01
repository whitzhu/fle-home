from django.contrib import admin
from django.contrib.auth.models import User

from models import UserResource, DeploymentStory


class UserResourceAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", "version")}
	list_display = ('title', 'version', 'doc_url', 'publish_date',)

class DeploymentStoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

admin.site.register(UserResource, UserResourceAdmin)
admin.site.register(DeploymentStory, DeploymentStoryAdmin)

