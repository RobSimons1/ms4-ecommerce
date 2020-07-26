from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Item
from .forms import ItemForm
from django.contrib import messages
from products.models import Product # Imported for product specific review
from datetime import datetime

# Create your views here.

def get_review_list(request, id):
    product = get_object_or_404(Product, pk=id)
    results = Item.objects.filter(date__lte=datetime.now()).order_by('-date')
    return render(request, "user_reviews.html", {
        'product': product,
        'items': results

    })    

def create_an_item(request, id):
    product = get_object_or_404(Product, pk=id)
    results = Item.objects.filter(date__lte=datetime.now()).order_by('-date')
    if request.method == "POST":
        new_item = ItemForm(request.POST) # post the new_item to the ItemForm
        if new_item.is_valid():
            new_item.instance.name = request.POST.get('name') # instance passes keyword argument to the model whose relations will be edited in the formset
            new_item.instance.beer = request.POST.get('beer')
            new_item.instance.review = request.POST.get('review')
            new_item.instance.rating = request.POST.get('rating')
            new_item.instance.done = 'done' in request.POST
            new_item.save()
        messages.success(request, 'Thankyou for your review')

        return render(request, "user_reviews.html", {
        'new_item': new_item,
        'product': product,
        'items': results
    })

    return render(request, "user_ratings.html")