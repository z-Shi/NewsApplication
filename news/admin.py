from django.contrib import admin
from news.models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ('heading', 'publication_date', 'content')


admin.site.register(Story, StoryAdmin)
