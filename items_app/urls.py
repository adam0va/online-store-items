from django.conf.urls import url
from items_app import views

urlpatterns = [
    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',
        views.ItemDetail.as_view()),
]