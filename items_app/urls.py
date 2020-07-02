from django.conf.urls import url
from items_app import views

urlpatterns = [
    url(r'^$', views.ItemList.as_view()),
    url(r'^(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',
        views.ItemDetail.as_view()),
    url(r'^by_category/?P<category>(Lipstick)|(Mascara)|(Foundation)|(Powder)|(Blush)|(Eyeliner)$',
        views.ItemList.as_view()),
]