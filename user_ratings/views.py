from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Review
from .forms import ItemForm
from django.contrib import messages
from products.models import Product
from django.utils import timezone

# Create your views here.


def get_review_list(request, id):
    product = get_object_or_404(Product, pk=id)
    reviews = Review.objects.all().filter(
        product=product, date__lte=timezone.now()).order_by('-date')
    return render(request, "user_reviews.html", {
        'product': product,
        'items': reviews

    })


def create_an_item(request, id):
    product = get_object_or_404(Product, pk=id)

    reviews = Review.objects.all().filter(
        product=product, date__lte=timezone.now()).order_by('-date')
    if request.method == "POST":
        new_item = ItemForm(request.POST)  # post the new_item to the ItemForm
        if new_item.is_valid():
            form = ItemForm(request.POST)
            new_item.instance.name = request.POST.get('name')
            new_item.instance.review = request.POST.get('review')
            new_item.instance.rating = request.POST.get('rating')

            new_item.save()
            messages.success(request, 'Thankyou for your review')

        return render(request, "user_reviews.html", {
            'product': product,
            'items': reviews

        })

    return render(request, "user_ratings.html", {
        'product': product, 'items': reviews})
