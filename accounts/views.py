from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.




def http_login(request):
    

    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request,"login successful")
                return redirect('/')
                
            else:
                messages.error(request,'wrong input, check your details.')
                return redirect('/accounts/login')

        form=AuthenticationForm()
        context={'form':form}
        return render(request, 'accounts\login.html',context) 
    else:
        return HttpResponse('sen varsin')




@login_required
def http_logout(request):
    logout(request)
    return redirect('/')
    
