from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about),
    path('form/',views.form, name='form'),
    path('contact/',views.contact),
]