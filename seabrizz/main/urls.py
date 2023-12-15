from django.urls import path

from seabrizz import settings
from . import views
from django.conf.urls.static import static


urlpatterns =[
    path('', views.index, name = "home"),
    path('add', views.add, name = "add_form"),
    path('<int:pk>/delete', views.Delete.as_view(), name='sea-del'),
    path('<int:pk>/update', views.Update.as_view(), name='sea-update'),
    path('abouts', views.about, name = "about"),
    path('shedules', views.shedule, name = "shedule")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)