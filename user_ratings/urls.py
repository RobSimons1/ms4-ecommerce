from django.conf.urls import url
from .views import get_review_list, create_an_item

urlpatterns = [
    url(r'^get_review_list/$', get_review_list),
    url(r'^add/$', create_an_item), # user_ratings urls import
] 