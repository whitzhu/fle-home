from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from models import UserResource, DeploymentStory, Gallery, Picture


class UserResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "version")}
    list_display = ('title', 'version', 'doc_id', 'filename')

class DeploymentStoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "deployment_city")}
    list_display = ("contact_name", "title", "deployment_city", "deployment_country", "start_date", "number_of_photos", "published", "view_link")
    list_filter = ("published", "deployment_country", "start_date")

    def queryset(self, request):
        qs = super(DeploymentStoryAdmin, self).queryset(request)
        qs = qs.annotate(models.Count('photo_gallery__photos'))
        return qs

    def view_link(self, obj):
        url = obj.get_absolute_url()
        if not url:
            return ""
        return u"<a href='%s' target='_blank'>#%s</a>" % (url, obj.slug)
    view_link.short_description = "View!"
    view_link.allow_tags = True

    def number_of_photos(self, obj):
        return obj.photo_gallery__photos__count
    number_of_photos.admin_order_field = 'photo_gallery__photos__count'

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
                'published',
            )
        }),
        ('Bonus Options (not required)', {
            'fields': (
                'testimonials',
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
                'photo_gallery',
                'internal_notes',
            )
        }),
    )

class PictureInline(admin.TabularInline):
    model = Picture

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [
        PictureInline,
    ]

class PictureAdmin(admin.ModelAdmin):
    list_display = ('caption', 'title', 'gallery')

admin.site.register(UserResource, UserResourceAdmin)
admin.site.register(DeploymentStory, DeploymentStoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Picture, PictureAdmin)

