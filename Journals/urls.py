
from django.contrib import admin
from django.urls import path,include
from .views import *
app_name  = "Journals"
urlpatterns = [
    path('all/', journals_all , name = 'all'),
    path('<int:input_id>/', journals_by_id , name='byId'),
    path('new/' , journal_new , name='new'),
    path('<int:input_id>/edit/' , journals_edit , name='edit')
]
