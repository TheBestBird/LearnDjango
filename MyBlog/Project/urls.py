"""YourMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include

# urlpatterns - list with all first links by YourMap page.
# function path(link, function to use)
# with include function we could carry over to one of our templates (/blog here)
# Then we could use the same logic in templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]