from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.signout, name="logout"),
    path("addpost/", views.add_post, name="addpost"),
    path("editpost/<int:id>", views.edit_post, name="editpost"),
    path("deletepost/<int:id>", views.delete_post, name="deletepost"),

]