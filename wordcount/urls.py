
from django.urls import path
from . import view
urlpatterns = (
path('',view.homp,name='home'),
path('counter/',view.count,name='count')
)
