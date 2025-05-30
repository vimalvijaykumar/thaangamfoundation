"""config URL Configuration

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
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls), 
	path('', include('blog.urls')), # Blog App
	path('', include('accounts.urls')),  # Auth App
	path('auth/', include('django.contrib.auth.urls')), 
]


handler404 = 'blog.views.error_404'
# handler500 = 'blog.views.error_500'
handler403 = 'blog.views.error_403'
# handler400 = 'blog.views.error_400'
