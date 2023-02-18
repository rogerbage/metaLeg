# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('api', views.api, name='api'),
    path('updateDecretos', views.updateDecretos, name='updateDecretos'),
    path('updateOrdinarias', views.updateOrdinarias, name='updateOrdinarias'),
    path('cleanOrdinarias', views.cleanOrdinarias, name='cleanOrdinarias'),
    path('getDecreto', views.getDecreto, name='getDecreto'),
    path('getLeg', views.getLeg, name='getLeg'),
    path('cleanDecreto', views.cleanDecreto, name='cleanDecreto'),
    path('cleanDecretos', views.cleanDecreto, name='cleanDecreto'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
