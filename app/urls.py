from django.urls import path
from .views import home,loginPage,register,logoutPage,locations_list,place
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name="home"),


    path('register/',register,name="register"),
    path('login/',loginPage,name="login"),
    path('logout/',logoutPage,name="logout"),

    path('locations-list/', locations_list, name='locations'),
    path('place/<str:pk>/',place,name="place")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)