"""zengproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views
'''
    path('welcome/<str:username>', views.welcome),


    	path('', views.time_cookie),
	path('index/', views.time_cookie),

    path('delete_cookie/<str:key>/', views.delete_cookie),
    path('set_cookie/<str:key>/<str:value>/', views.set_cookie),
    path('set_cookie2/<str:key>/<str:value>/', views.set_cookie2),
    path('get_cookie/<str:key>/', views.get_cookie),
	path('get_allcookie/', views.get_allcookie),

	path('set_session/<str:key>/<str:value>/', views.set_session),
	path('set_session2/<str:key>/<str:value>/', views.set_session2),
	path('get_session/<str:key>/', views.get_session),
	path('get_allsession/', views.get_allsession),
	path('delete_session/<str:key>/', views.delete_session),
    path('kill_allsession/', views.kill_allsession),

	path('login/', views.login),	
	path('logout/', views.logout),	
    path('login/register/', views.register)
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.form),
    path('index/',views.index),
    path('dtform/',views.dtform),
    path('edit/<int:id>/',views.edit),
    path('edit/<int:id>/<str:mode>', views.edit),
    path('delete/<int:id>/',views.delete),
    path('postform/', views.postform),
    path('delete2/<str:name>/',views.delete2),

]