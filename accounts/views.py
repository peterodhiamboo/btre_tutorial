from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        #GET USER INPUT
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #VALIDATION
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered')
                    return redirect('register')
                else:
                    #ALL IS CLEAR, SAVE USER
                    user = User.objects.create_user(username=username, password=password, email=email, 
                    first_name=first_name, 
                    last_name=last_name)
                    #LOGIN AFTER REGISTER
                    #auth.login(request, user)
                    #messages.success(request, 'Account was created')
                    user.save()
                    messages.success(request, 'Account was created, you can now login')
                    return redirect('login')
        else:
            messages.error(request, 'PASSWORD MISMATCH !!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Incorrect credentials !')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been Logged out')
        return redirect('index')

def dashboard(request):
    user_listings = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_listings
    }

    return render(request, 'accounts/dashboard.html', context)


    

