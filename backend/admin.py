from django.contrib import admin

from . import models
# zzes klren0312

class Articleadmin(admin.ModelAdmin):

    list_display = ('title', 'time','admin_image')
    readonly_fields = ('admin_image',)
    search_fields = ('title', 'content')



admin.site.register(models.Article,Articleadmin)
