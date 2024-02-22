from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("hello2/", hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhome'),
    path('travelpackage',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/', print1,name='print1'),
    path('randomotp1/',randomcall,name='randomcall'),
    path('l/',randomlogic,name='randomlogic'),
    path('d/',getdate1,name='getdate1'),
    path("k/",getdate,name='getdate'),
    # path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    # path('tzfunctionlogic/',tzfunctionlogic,name='tzfunctionlogic'),
    path('registercallfunction/',registercallfunction,name='registercallfunctional'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('famous/',famous,name='famous'),
    path('weathercall/', weathercall, name='weathercall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contactfun/',contactfun,name='contactfun'),
    path('contactmail/',contactmail,name='contactmail'),
]