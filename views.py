from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import UserAdminCreationForm, ProfileForm


# @login_required()
# def register(req):
#     form = UserAdminCreationForm()
#     if req.method == 'POST':
#         form = UserAdminCreationForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home/register')
#     return render(req, 'accounts/register.html', {'form': form})

@login_required()
def register_view(request):
    if request.method == 'POST':
            register = UserAdminCreationForm(request.POST, prefix='register')
            usrprofile = ProfileForm(request.POST, prefix='profile')
            if register.is_valid() * usrprofile.is_valid():
                user = register.save()
                usrprof = usrprofile.save(commit=False)
                usrprof.user = user
                usrprof.set_token()
                usrprof.subscribed = '1'
                usrprof.save()
                return HttpResponse('congrats')
    else:
        register = UserAdminCreationForm(prefix='register')
        usrprofile = ProfileForm(prefix='profile')
        return render(request, 'accounts/register.html', {'userform': register, 'userprofileform': usrprofile})

def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'accounts/login1.html')


def logout(request):
    auth.logout(request)
    return render(request,'accounts/logout1.html')


def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')

    return render(request, 'accounts/admin1.html')

