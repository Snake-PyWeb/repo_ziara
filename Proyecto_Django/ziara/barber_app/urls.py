from django .urls import path
from barber_app import views

urlpatterns=[
    path('',views.index,name='index'),
]