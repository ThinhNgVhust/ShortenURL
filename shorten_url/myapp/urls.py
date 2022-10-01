from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("get-link",views.get_link,name="get-link"),
   
]