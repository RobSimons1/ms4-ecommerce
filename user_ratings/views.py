from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Review
from .forms import ItemForm
from django.contrib import messages
from products.models import Product # Imported for product specific review
from datetime import datetime

# Create your views here.

def get_review_list(request, id):
    product = get_object_or_404(Product, pk=id)
    reviews = Review.objects.all().filter(product=product)
    return render(request, "user_reviews.html", {
        'product': product,
        'items': reviews

    })    

def create_an_item(request, id):
    product = get_object_or_404(Product, pk=id)
    print("product -------------------------------", product.id)
    reviews = Review.objects.all().filter(product=product)
    if request.method == "POST":
        print("POST request received! *************************")
        new_item = ItemForm(request.POST) # post the new_item to the ItemForm
        print(f"new_item: {new_item}")
        print(f"request.POST.get('product'): {request.POST.get('product')}")
        print(f"request.POST.get('name'): {request.POST.get('name')}")
        print(f"request.POST.get('review'): {request.POST.get('review')}")
        print(f"request.POST.get('rating'): {request.POST.get('rating')}")
        if new_item.is_valid():
            print("form is valid!")
            form = ItemForm(request.POST) 
            print(f"form is: {form}")
            print(f"new_item.instance: {new_item.instance}")
            # new_item.instance.product = product.id
            new_item.instance.name = request.POST.get('name') # instance passes keyword argument to the model whose relations will be edited in the formset
            new_item.instance.review = request.POST.get('review')
            new_item.instance.rating = request.POST.get('rating')
            #reviews = Review.objects.get(Product, pk=id)
            #form = ItemForm(request.POST, instance=reviews)
            print(f"form after 'form = ItemForm(request.POST, instance=reviews)' {form}")
            #form.save()
            print(f"new_item before saving it: {new_item}")
            new_item.save()
            messages.success(request, 'Thankyou for your review')
        else:
            print("############## form IS NOT VALID !!!!!!!!!!!!!!!!")
        return render(request, "user_reviews.html", {
        'new_item': new_item,
        'product': product,
        'items': reviews
        
    })

    return render(request, "user_ratings.html", {'product': product, 'items': reviews }) # Pass through context in GET method to display form. 