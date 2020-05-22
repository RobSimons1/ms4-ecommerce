from django.shortcuts import render

# Create your views here.
def contact(request):
    """A view that diplays the contact page"""
    return render(request, "contact.html")

