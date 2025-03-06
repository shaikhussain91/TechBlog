from django.urls import path
from .views import *  # Import all views

app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('login/', loginview, name='login'),  
    path('logout/', logoutview, name='logout'),  
    path('createacc/', createacc, name='createacc'),
    path('blog/', blog, name='blog'),
    path('main/', main, name='main'),
    path('profile/', profile, name='profile'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),
    path('about/', about, name='about'),
    path('blog/update/<int:id>/', update, name='update'),
    path('blog/delete/<int:id>/', delete, name='delete'),
  
  
]

