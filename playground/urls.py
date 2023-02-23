from django.urls import path
from playground import views
from django.conf import settings
from django.conf.urls.static import static

app_name="first_app"

urlpatterns = [
    path('',views.index,name='index'),
    path('add_album/',views.album_form,name='album_form'),
    path('add_musician/',views.musician_form,name='musician_form')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)