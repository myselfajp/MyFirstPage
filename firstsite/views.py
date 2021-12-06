from django.http.response import HttpResponse
from django.shortcuts import render

from firstsite.forms import NameForm

def http_home(request):
    return render(request,"firstsite\Index.html")
    
def http_contact(request):
    return render(request,"firstsite\Contact.html")

def http_about(request):
    return render(request,"firstsite\About.html")

def http_elements(request):
    return render(request,"firstsite\Elements.html")

def http_test(request):
    if request.method== 'POST':
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            return HttpResponse('name= %s <br> email= %s <br> subject= %s <br> message= %s'%(name,email,subject,message))
        else:
            return HttpResponse('not valid')
    form = NameForm()
    return render(request,"test.html",{'form':form})





