from django.urls import path

from shop_account.views import login_page, register_page, log_out, user_panel, edit_profile, edit_password

urlpatterns = [
    path("login", login_page),
    path("register", register_page),
    path("log-out", log_out),
    path("user-panel", user_panel),
    path("user-panel/edit", edit_profile),
    path("user-panel/edit-password", edit_password),
]
