from django.urls import path
from playground import views
from django.conf import settings
from django.conf.urls.static import static

app_name="first_app"

urlpatterns = [
    path('',views.index,name='index'),
    path('add_album/',views.album_form,name='album_form'),
    path('add_musician/',views.musician_form,name='musician_form'),
    path('album_list/<int:id>/',views.album_list,name='album_list'),
    path('edit_artist/<int:id>/',views.edit_artist,name='edit_artist'),
    path('edit_album/<int:id>/',views.edit_album,name='edit_album'),
    path('delete_album/<int:id>/',views.delete_album,name='delete_album'),
    path('delete_musician/<int:id>/',views.delete_musician,name='delete_musician'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)