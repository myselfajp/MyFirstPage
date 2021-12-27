from django.shortcuts import redirect ,render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import signup_form


def http_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,'Login successfull .')
                return redirect('/')
            else:
                messages.error(request,"username or password is incorrect.")
    else:
        return redirect('/')
    return render(request, 'accounts/login.html')



def http_signup(request):
    if not request.user.is_authenticated:
        form=signup_form()
        if request.method == 'POST':
            form=signup_form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully created , you can log in now")
                return redirect('/accounts/login')
    else:
        return redirect('/')

    context={'form':form}
    return render(request, 'accounts/signup.html', context)

    

@login_required
def http_logout(request):
    logout(request)
    return redirect('/')
    
