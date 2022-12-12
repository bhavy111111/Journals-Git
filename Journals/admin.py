from django.contrib import admin

from .models import Journal

class JournalAdmin(admin.ModelAdmin):
	list_display = ['title' , 'timestamp','text_field']
	search_fields = ['title']
	list_display_links = ['title']

admin.site.register(Journal,JournalAdmin)