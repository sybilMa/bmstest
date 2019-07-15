"""rstful_day05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
from rest_framework.routers import SimpleRouter,DefaultRouter

#SimpleRouter 自动生成两条路由
#DefaultRouter自动生成四条路由
# router=SimpleRouter()
# router=DefaultRouter()
# router.register('publish',views.PublishView)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<version>[v1|v2]+)/publish/', views.PublishView.as_view()),
    # url(r'^publish/$', views.PublishView.as_view({'get':'list','post':'create'})),
    # url(r'^publish\.(?P<format>\w+)$', views.PublishView.as_view({'get':'list','post':'create'})),
    # url(r'^publish/(?P<pk>\d+)$', views.PublishView.as_view({'get':'retrieve','delete':'destroy','put':'update'})),
    # url(r'', include(router.urls)),
]
