from django.shortcuts import render

def http_home(request):
    return render(request,"firstsite\Index.html")
    
def http_contact(request):
    return render(request,"firstsite\Contact.html")

def http_about(request):
    return render(request,"firstsite\About.html")

def http_elements(request):
    return render(request,"firstsite\Elements.html")





