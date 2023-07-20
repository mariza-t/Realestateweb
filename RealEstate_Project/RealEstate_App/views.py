from django.shortcuts import render
from .models import *
# Create your views here.


def home_view(request):
    readme_list = Readme.objects.all()
    agent_list = Agentdetail.objects.all()
    comment_list = Comment.objects.all()
    appoint = Apointment.objects.all()
    data={'readme_list':readme_list,'agent_list':agent_list,'comment_list':comment_list,'appoint':appoint}


    if request.method == "POST":
        first_name1 =request.POST.get('first_name1')
        last_name1 =request.POST.get('last_name1')
        email1 =request.POST.get('email1')
        phone1 =request.POST.get('phone1')
      

        obj=Apointment()
        obj.first_name1 =first_name1
        obj.last_name1=last_name1
        obj.email1=email1
        obj.phone1=phone1
        obj.save()
       
    return render(request, "index.html", data)

def about(request):
    comment_list = Comment.objects.all()
    readme_list = Readme.objects.all()
    data={'comment_list':comment_list,'readme_list':readme_list}

    return render(request,"about.html",data)

def contact(request):
    comment_list = Comment.objects.all()
    data={'comment_list':comment_list}
    if request.method == "POST":
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        comments =request.POST.get('comments')

        obj=Request_for_Contact()
        obj.first_name =first_name
        obj.last_name=last_name
        obj.email=email
        obj.phone=phone
        obj.comments=comments
        obj.save()
    return render(request,"contact.html",data)
    
    

def service_view(request):
    service_list =Services.objects.all()
    comment_list = Comment.objects.all()
    data = {'service_list':service_list,'comment_list':comment_list}

    return render(request, "service.html" , data)

def gallery_view(request):
    gallery_list =Gallery.objects.all()
    comment_list = Comment.objects.all()
    data = {'gallery_list':gallery_list,'comment_list':comment_list}

    return render(request, "gallery.html" , data)

def Property_detail_view(request):
    Property_list =Property_detail.objects.all()
    comment_list = Comment.objects.all()
    data = {'Property_list':Property_list,
            'comment_list':comment_list}

    return render(request, "properties.html" , data)

   
