from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path("cart-item", views.add_to_cart, name="add-to-cart"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name= "register"),
    path("get-pizza-price", views.get_pizza_price, name="get-pizza-price"),
    path("clear-cart", views.clear_cart, name="clear-cart"),
    path("checkout", views.checkout_view, name="checkout"),
    path("details", views.get_item_details, name="details")
]
