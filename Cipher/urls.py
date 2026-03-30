from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path("blog/", views.blog, name="blog"),
    path('add-theory/', views.add_theory, name='add_theory'),
    path('theories/', views.theories, name='theories'),
    path('edit-theory/<int:id>/', views.edit_theory, name='edit_theory'),
    path('delete-theory/<int:id>/', views.delete_theory, name='delete_theory'),




]