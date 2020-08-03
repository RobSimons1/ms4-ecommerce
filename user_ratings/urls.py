from django.conf.urls import url
from .views import get_review_list, create_an_item
from products.views import all_products

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^get_review_list/(?P<id>\d+)',
        get_review_list, name="get_review_list"),
    url(r'^add/(?P<id>\d+)', create_an_item, name="create_an_item"),
]
