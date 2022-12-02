from django.urls import path
from . import views
from .views import Blogdetail, Bloghome
app_name='index'
urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('updateitem/', views.updateitem, name='updateitem'),
    path('s_and_t/', views.s_and_tlist, name='s_and_t'),
    path('blog/', views.blogger, name='blogger'),
    path('bloghome/', Bloghome.as_view(), name='bloghome'),
    path('article/<int:pk>', Blogdetail.as_view(), name='blogdetail'),
    path('services/', views.services, name='services'),
    path('tools/', views.tools, name='tools')
]
