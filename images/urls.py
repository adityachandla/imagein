from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	path('',views.home,name="home"),
	path('image/<int:pk>', views.image,name="image"),
	path('putlike/<int:pk>',views.putLike, name="putLike")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)