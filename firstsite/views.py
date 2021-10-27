from django.shortcuts import render

def http_home(request):
    return render(request,"firstsite\Home.html")
    
def http_contact(request):
    return render(request,"firstsite\Contact.html")


def http_about(request):
    return render(request,"firstsite\About.html")

