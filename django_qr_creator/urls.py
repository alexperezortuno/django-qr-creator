from django.urls import re_path, path

from . import views

app_name = 'django_qr_creator'

urlpatterns = [
    path('demo/url', views.qr_url, name='qr_url'),
    re_path(r'^(?P<param_data>[0-9A-z-.@]{1,})/qr.(?P<extension>(png)|(svg)|(jpg))$', views.image_with_vars, name='image_with_vars'),
]
