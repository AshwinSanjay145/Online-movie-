from . import views
from django.urls import path, include

app_name='movie'
urlpatterns = [
    path('',views.home,name="home"),
    path('movie/<int:movie_id>',views.detail,name="detail"),
    path('add/',views.add_movie,name="addmovie"),
    path('edit/<int:id>',views.update,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
]
