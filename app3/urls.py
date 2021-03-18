from django.urls import path
app_name='app3'
from app3 import views
urlpatterns=[
    
    path('ms/',views.by,name='ms'),
    path('bunty/',views.hi,name='bunty')

]