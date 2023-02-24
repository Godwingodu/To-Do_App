from django.urls import path
from .views import * 
from app.views import Home


urlpatterns = [

    path('', Home, name='home'),
    path('login/',Login, name='login'),
    path('signup/',Signup, name='signup'),
    path('logout/',Logout, name='logout'),
    path('viewtodo/',ViewTodo, name='viewtodo'),
    path('addtodo/',AddTodo, name='addtodo'),
    path('deletetodo/<int:id>',DeleteTodo, name='deletetodo'),
    path('edittodo/<int:id>',EditTodo, name='edittodo'),
    path('search/',search, name='search')






]