from django.http.response import HttpResponse
from django.shortcuts import render

from firstsite.forms import ContactForm

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
        form=ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Name= %s\nEmail= %s\nSubject= %s\nMessage= \n%s '%(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['subject'],form.cleaned_data['message']),content_type="text/plain")
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request,"test.html",{'form':form})





