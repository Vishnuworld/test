"""book URL Configuration

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
from django.urls import path, include
from shelf import urls, views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token
from shelf.views import some_view, HelloView, login

#####
schema_view = get_swagger_view(title='Book_Producer')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', schema_view),
    url(r'^v1/', include('shelf.urls')),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('generate-token/', obtain_auth_token, name='api_token_auth'),
    path('api/login/', login)

    # path('pdf/', some_view, name='pdf'),

    # path('v/', views.hello, name='hello'),
]




