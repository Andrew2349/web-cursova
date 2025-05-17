"""
URL configuration for web_cursova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from network import views
from django.contrib.auth.views import LogoutView
from django.conf import settings  # імпорт settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('create/', views.create_post, name='create_post'),

    path('search/', views.search, name='search'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('settings/', views.site_settings, name='settings'),
path('add_comment/', views.add_comment, name='add_comment'),
path('friends/', views.friends_list, name='friends'),
path('friends/search/', views.find_friends, name='find_friends'),
    path('friends/add/<int:user_id>/', views.add_friend, name='add_friend'),
path('friends/accept/<int:user_id>/', views.accept_friend, name='accept_friend'),
path('friends/remove/<int:user_id>/', views.remove_friend, name='remove_friend'),
path('friends/reject/<int:user_id>/', views.reject_friend, name='reject_friend'),
    path('routes/', views.routes, name='routes'),
    path('routes/create/', views.create_route, name='create_route'),
    path('routes/<int:route_id>/', views.route_detail, name='route_detail'),
    path('add_route_comment/', views.add_route_comment, name='add_route_comment'),
    path('notifications/', views.notifications, name='notifications'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)