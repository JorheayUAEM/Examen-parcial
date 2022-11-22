from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.inicio, name='inicio'),
    re_path(r'^registros/', views.datos_list, name='registros'),
    re_path(r'^KNN/', views.buscar, name='algoritmo_knn'),
    re_path(r'^CBI/', views.alg_cbi, name='algoritmo_cbi'),
    re_path(r'^REGRESION/', views.regresionLog, name = 'algoritmo_regLog'),
    re_path(r'^RESULTRL/', views.interpretar, name = 'result_regLog'),
]