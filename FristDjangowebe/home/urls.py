from django.urls import path
from . import views
app_name='home'
urlpatterns=[
    path('',views.page1,name='home'),
    path('page2',views.page2),
]