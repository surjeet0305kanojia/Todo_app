
from django.contrib import admin
from django.urls import path
from application import views
urlpatterns = [
    path('',views.home ,name='home'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup),
    path('add-todo/',views.add_todo),
    path('logout/',views.signout ),
    path('delete-todo/<int:id>', views.delete_todo ),
    path('change-status/<int:id>/<str:status>', views.change_todo ),
]
  