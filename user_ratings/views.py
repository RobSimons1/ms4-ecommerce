from django.shortcuts import render, HttpResponse, redirect
from .models import Item


def create_an_item(request):
    if request.method == "POST":
        new_item = Item()
        new_item.name = request.POST.get('name')
        new_item.done = 'done' in request.POST
        new_item.save()

        return redirect(create_an_item)

    return render(request, "user_ratings.html")
