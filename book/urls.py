from django.urls import path
from . import views  

app_name = "book"
urlpatterns = [
    path('', views.index, name='index'),
    path('tabadd/' , views.tab_add , name="tabadd"),
] 