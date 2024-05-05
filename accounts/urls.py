from django.urls import path
from accounts.views import user_login, user_logout, user_register, index_view, whatsapp_login, Contact_Us, about_us, product


urlpatterns = [
    path('', index_view, name='home'),
    path('login/', user_login, name='login'),
    path('about/',about_us, name='about'),
    path('products/',product, name='product'),
    path('contact',Contact_Us.as_view(), name='contact' ),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path("whatsapp-login/", whatsapp_login, name="whatsapp-login"), 

]
