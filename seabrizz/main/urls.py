from django.urls import path

from seabrizz import settings
from . import views
from django.conf.urls.static import static


urlpatterns =[
    path('', views.index, name = "home"),
    path('/add', views.add, name =  "add")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)