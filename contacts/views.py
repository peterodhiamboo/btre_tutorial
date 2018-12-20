from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if has_inquired:
                messages.error(request, 'Sorry, you cant resubmitt an inquiry')
                return redirect('/listings/'+listing_id)
            else:
                contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message,user_id=user_id)
                contact.save()
                messages.success(request, 'Request submitted. A realtor will get back to you shortly')
                return redirect('/listings/'+listing_id)   
        else:
            contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message,user_id=user_id)
            contact.save()
            messages.success(request, 'Request submitted. A realtor will get back to you shortly')
            return redirect('/listings/'+listing_id)
        