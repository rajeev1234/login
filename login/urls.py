"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from landingpage.views import signup,home
from newsletters.views import Newsletter

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('signup/',signup,name='signup'),
    path('',home,name='home'),
    path('post/',include('post.urls'),name='post'),
    path('newsletter/',Newsletter,name='newsletter'),
    path('enquiry/',include('enquiry.urls')),
    path('contact_us/',include('contactus.urls')),
    path('services/',include('services.urls')),
    path('past_work/',include('Past_Work.urls')),
    path('work/',include('Work.urls')),


]
