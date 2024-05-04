from django.urls import path
from accounts.views import user_login, user_logout, user_register, index_view


urlpatterns = [
    path('', index_view, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
]
