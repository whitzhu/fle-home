from django.contrib import admin
from django.contrib.auth.models import User

from models import TeamMember, BoardMember, PressArticle, PressLogo, Internship


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'last_updated',)

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'last_updated',)


class PressArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publish_date',)

class PressLogoAdmin(admin.ModelAdmin):
	list_display = ('title',)

class InternshipAdmin(admin.ModelAdmin):
	list_display = ('title', 'last_updated')

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(PressArticle, PressArticleAdmin)
admin.site.register(PressLogo, PressLogoAdmin)
admin.site.register(Internship, InternshipAdmin)

