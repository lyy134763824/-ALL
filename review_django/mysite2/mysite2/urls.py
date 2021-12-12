"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path

from mysite2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$', views.index_view),
    # path(r'pagen_calculate/<int:n1>/<str:symbol>/<int:n2>', views.page_calculate),
    path(r'page/<int:page>', views.pagen_view),
    re_path(r'^(?P<n1>\d+)/(?P<symbol>\w+)/(?P<n2>\d+)$',views.page_calculate),
    re_path(r'^test_request',views.test_view),
    re_path(r'^test_post',views.test_post),
]
