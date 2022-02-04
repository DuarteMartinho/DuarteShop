from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.home, name="home"),
   path('product/<int:prodId>', views.product_individual, name="product_individual"),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/',views.UserLoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('addbasket/<int:prodid>', views.add_to_basket, name="add_basket"),
   path('basket/', views.show_basket, name="show_basket"),
]