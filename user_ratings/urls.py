from django.conf.urls import url
from .views import create_an_item

urlpatterns = [
    url(r'^add$', create_an_item), # user_ratings urls import 
] 