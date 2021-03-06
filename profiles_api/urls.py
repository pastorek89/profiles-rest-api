from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #w ViewSet bedzie widoczne tylko to co jest dodane do routera i nic wiecej
router.register('profile', views.UserProfileViewSet) #nie trzeba base_name poniewaz mamy w ModelViewSet queryset object. DRF daje imie od razu

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #to nie bedzie widoczne
    path('', include(router.urls))
]