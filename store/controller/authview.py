from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User register successful")
            return redirect('login')
        
    context = {'form':form}
    return render(request,'store/auth/register.html',context) 

def login_page(request):
    if request.user.is_authenticated:
        messages.warning(request,'Already logged in !')
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request,'login successful')
                return redirect('/')
            else:
                messages.error(request,'login failed')
                return redirect('login')
        return render(request,'store/auth/login.html')
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'logout successful')
        return redirect('/')
    else:
        messages.error(request,'logout failed')
        return redirect('/')