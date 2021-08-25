from django.urls import path
from .import views
urlpatterns = [

    path('EntryD/',views.EntryD,name='EntryD'),
    path('EntryD/Final/',views.Final,name='Final'),
    path('',views.index,name='index'),
    path('End/',views.End,name='End')
]
