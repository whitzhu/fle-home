from django.contrib import admin
from django.contrib.auth.models import User

from models import UserResource, DeploymentStory, Gallery, Picture


class UserResourceAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", "version")}
	list_display = ('title', 'version', 'doc_url', 'publish_date',)

class DeploymentStoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", "deployment_city")}
	list_display = ('title', 'deployment_country', 'contact_name')

	fieldsets = (
		(None, {
			'fields': (
				'title',
				'slug', 
				'contact_name', 
				'contact_email', 
				'start_date', 
				'deployment_city', 
				'deployment_country', 
				'latitude', 
				'longitude', 
				'description', 
			)
		}),
		('Bonus Options (not required)', {
			'fields': (
				'organization_name',
				'organization_url',
				'organization_city',
				'organization_country',
				'num_students',
				'student_age_range',
				'num_kalite_servers',
				'server_os',
				'hardware_setup',
				'deployment_setting',
				'pedagogical_model',
				'guest_blog_post',
				'photo_gallery'
			)
		}),
	)	

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

class PictureAdmin(admin.ModelAdmin):
	list_display = ('title', 'gallery')

admin.site.register(UserResource, UserResourceAdmin)
admin.site.register(DeploymentStory, DeploymentStoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Picture, PictureAdmin)

