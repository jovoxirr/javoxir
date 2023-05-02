from django.urls import path
from .views import Home, Contact, About, Login, ProductDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact', Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('login', Login.as_view(), name='login'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail')
]
