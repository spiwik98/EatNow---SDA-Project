from django.urls import path, include
from register import views as v


urlpatterns = [
    path('register/', v.register, name='register'),
    path('logout/', v.logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
]
