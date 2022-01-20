from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('list/', ElementosList.as_view()),
    path('create/', ElementoCreate.as_view()),
    re_path('^detail/(?P<Nombre>.+)/$', ElementoDetail.as_view()),
    re_path('^delete/(?P<Nombre>.+)/$', ElementoDelete.as_view()),
    re_path('^update/(?P<Nombre>.+)/$', ElementoUpdate.as_view()),
    path('categoria/', CategoriaList.as_view()),
    path('filter/', ElementoListFilter.as_view())
]