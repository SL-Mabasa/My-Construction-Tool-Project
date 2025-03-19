from django.urls import path
from . import views

#URL config
urlpatterns = [
    path('', views.intro),
    path('Home', views.home),
    path('About', views.about),
    path('Contact', views.contact),
    path('Tools', views.tools),
    path('vo.html', views.vo),
    path('table.html', views.table),
    path('Materials', views.materials),
    path('Products', views.products),
    path('Battery', views.battery),
    path('Inverter', views.inverter),
    path('Panels', views.panel),
    path('DEV', views.dev),
]
