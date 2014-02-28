from django.contrib import admin
from django.contrib.auth.models import User

from models import AboutSection, TeamMember, BoardMember, PressArticle


class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'last_updated',)

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'last_updated',)


class PressArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publish_date',)

  
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(PressArticle, PressArticleAdmin)

