from django.contrib import admin

from .models import Journal

class JournalAdmin(admin.ModelAdmin):
	list_display = ['id','title' , 'timestamp','text_field' , 'image']
	search_fields = ['title']
	list_display_links = ['title']

admin.site.register(Journal,JournalAdmin)