from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm
from django.contrib import messages

# Create your views here.
def get_review_list(request):
    results = Item.objects.all()
    return render(request, "user_reviews.html", {
        'items': results
    })

def create_an_item(request):
    if request.method == "POST":
        new_item = Item()
        new_item.name = request.POST.get('name')
        new_item.done = 'done' in request.POST
        new_item.save()
        messages.success(request, 'Thankyou for your review')

        return redirect(get_review_list)

    return render(request, "user_ratings.html")
