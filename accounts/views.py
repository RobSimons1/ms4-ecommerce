from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm, ContactForm, OrderForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import sys # imported to view print outs of Contat Form message in Heroku

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def contact(request):
    """A view that allows the user to send and email message redirects back to the contact page"""
    if request.method == 'POST':  # If the form has been submitted...
        user_form = ContactForm(request.POST)  # A form bound to the POST data
        if user_form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print(user_form.cleaned_data['user_email'])
            print(user_form.cleaned_data['message'])
            sys.stdout.flush() # Added in to show Heroku log print out

            messages.success(request, "Your message was successfully sent")

            send_mail(
                request.POST['user_email'], # user email displays in subject field and can be responded to                
                request.POST['message'], # body of message 
                "Blindside Brewing", # name of company appears in from_email field to know where email has derived from          
                ['rob.simons79@gmail.com'], # email_to recipiant 
                fail_silently=False,
            )

            return HttpResponseRedirect('/accounts/contact/') # Redirect after POST
    else:
        user_form = ContactForm()  # An unbound form

    return render(request, 'contact.html', {
        'user_form': user_form,
    })

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    order_form = OrderForm()
    if request.method == "POST":
        order_form = OrderForm(request.POST)        

    return render(request, "profile.html", {"order_form": order_form})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
