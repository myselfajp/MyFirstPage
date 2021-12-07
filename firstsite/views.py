from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from firstsite.forms import ContactForm,NewsLetterForm
from firstsite.models import NewsLetter
from django.contrib import messages




def http_about(request):
    return render(request,"firstsite\About.html")


def http_elements(request):
    return render(request,"firstsite\Elements.html")


def http_home(request):
    return render(request,"firstsite\Index.html")




def http_contact(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form=form.save()
            form.name="unknown"
            form.save()
            messages.success(request,'Your ticket sent.')
        else:
            messages.error(request,'Your ticket did\'nt sent.')
    return render(request,"firstsite\Contact.html")





def http_newsletter(request):
    if request.method == 'POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            check=NewsLetter.objects.filter(email=form.cleaned_data['email'])
            if not check:
                form.save()
                messages.success(request,'Your ticket sent.')
                return HttpResponseRedirect("/")
            else:
                messages.error(request,'you are saved already.')
                return HttpResponseRedirect("/")
        else:
            messages.error(request,'you are saved already.')
            return HttpResponseRedirect("/")





def http_test(request):
    if request.method== 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Name= %s\nEmail= %s\nSubject= %s\nMessage= \n%s '%(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['subject'],form.cleaned_data['message']),content_type="text/plain")
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request,"test.html",{'form':form})
