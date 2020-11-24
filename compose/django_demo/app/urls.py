# _*_ encoding:utf-8 _*_
__author__ = 'nzb'
__datetime__ = '2020/11/24 13:51'
__doc__ = ''
from django.urls import path

from app.views import Info, Debug, Error

urlpatterns = [
    path('info', Info.as_view(), name='info'),
    path('error', Error.as_view(), name='error'),
    path('debug', Debug.as_view(), name='debug'),
]