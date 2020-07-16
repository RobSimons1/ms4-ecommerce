from django.conf.urls import url
from .views import get_todo_list, create_an_item

urlpatterns = [
    url(r'^get_todo_list', get_todo_list),
    url(r'^add$', create_an_item), # user_ratings urls import
] 