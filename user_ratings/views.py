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
        new_item = ItemForm(request.POST) # post the new_item to the ItemForm
        if new_item.is_valid():
            new_item.instance.name = request.POST.get('name') # instance passes keyword argument to the model whose relations will be edited in the formset
            new_item.instance.beer = request.POST.get('beer')
            new_item.instance.review = request.POST.get('review')
            new_item.instance.done = 'done' in request.POST
            new_item.save()
        messages.success(request, 'Thankyou for your review')

        return redirect(get_review_list)

    return render(request, "user_ratings.html")
