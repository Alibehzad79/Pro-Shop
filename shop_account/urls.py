from django.urls import path

from shop_account.views import login_page, register_page, log_out, edit_password, edit_profile, user_panel

urlpatterns = [
    path("login", login_page),
    path("register", register_page),
    path("log-out", log_out),
    path("user-panel", user_panel),
    path("user-panel/edit", edit_profile),
    path("user-panel/edit-password", edit_password),
]
