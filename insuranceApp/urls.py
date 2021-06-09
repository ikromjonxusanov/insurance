from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    # path("service/<str:pk>", serviceClassView, name="serviceView"),
    # path("service/create/", serviceClassCreate, name="serviceCreate"),
    # path("service/update/<str:pk>", serviceClassUpdate, name="serviceUpdate"),
    # path("service/delete/<str:pk>", serviceClassDelete, name="serviceDelete"),
    path("news/", newsList, name='news'),
    path("news/create/", newsCreate, name='newsCreate'),
    path("news/view/<str:pk>/", newsView, name='newsView'),
    path("news/update/<str:pk>", newsUpdate, name='newsUpdate'),
    path("news/delete/<str:pk>", newsDelete, name='newsDelete'),
    path('kodeks/', kodeks, name="codex"),
    path('contact/', contact, name='contact'),
    path('contact/list/', contactList, name='contactList'),

    path('locations/', locations, name='locations'),
    path('locations/create/', locationsCreate, name='locationsCreate'),
    path('locations/update/<str:pk>/', locationsUpdate, name='locationsUpdate'),
    path('locations/delete/<str:pk>/', locationsDelete, name='locationsDelete'),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)