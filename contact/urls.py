from django.conf.urls import url, include
from .views import contact

urlpatterns = [
    url(r'^$', contact, name="contact"),
]