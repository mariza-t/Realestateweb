from django.shortcuts import render, get_object_or_404, redirect
from RealEstate_App.models import *
# from django import forms
from django.views.generic import TemplateView
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages



from RealEstate_App.models import *

class AboutView(TemplateView):
     form_class = readmeform
     form_class1= agentform
     form_class3= commentform
     form_class4= serviceform
     form_class5= galleryform
     form_class6= propertydetailform
     form_class7= contactform
     form_class8= appointemntform
     form_class9= selledform
     form_class10= rentalform
     form_class11= customerform
 
     initial = {"key": "value"}
     template_name = "myadmin/home.html"

     def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        form1= self.form_class1(initial=self.initial)
        form3= self.form_class3(initial=self.initial)
        form4= self.form_class4(initial=self.initial)
        form5= self.form_class5(initial=self.initial)
        form6= self.form_class6(initial=self.initial)
        form7= self.form_class7(initial=self.initial)
        form8= self.form_class8(initial=self.initial)
        form9= self.form_class9(initial=self.initial)
        form10= self.form_class10(initial=self.initial)
        form11= self.form_class11(initial=self.initial)
        return render(request, self.template_name, {"form": form,"form1":form1,
                                                    "form3":form3 ,"form4":form4,"form5":form5,"form6":form6,
                                                    "form7":form7,"form8":form8,"form9":form9,"form10":form10,
                                                    "form11":form11 })
     def post(self, request, *args, **kwargs):
        if request.method =='POST':
           form = self.form_class(request.POST)
           if form.is_valid():
             form.save()
            # <process form cleaned data>
             return redirect('admin1')

        return render(request, self.template_name, {"form": form})
     
     def post1(self, request, *args, **kwargs):
         if request.method =='POST':
            form1 = self.form_class2(request.POST) in request.FILES and request.FILES['file']
            if form1.is_valid():
             form1.save()
            # <process form cleaned data>
             return redirect('admin1')

         return render(request, self.template_name, {"form1": form1})
    
     
     def post3(self, request, *args, **kwargs):
         if request.method =='POST':
            form3 = self.form_class3(request.POST)in request.FILES and request.FILES['file']
            if form3.is_valid():
             form3.save()
            # <process form cleaned data>
             return redirect('admin1')

            return render(request, self.template_name, {"form3": form3})
     

   
def service_form(request):
    seritems=Services.objects.all()
    form = serviceform(request.POST or None)
    if form.is_valid():
        form.save()
        form = serviceform()
    context = {
        'service':form,
        'seritems':seritems
    }
    return render(request, 'myadmin/addservice.html', context)

def gallery_form(request):
    picitems=Gallery.objects.all()
    form = galleryform(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        form = galleryform()
    context = {
        'gallery':form,
        'picitems':picitems
    }
    return render(request, 'myadmin/addimages.html', context)

def property_form(request):
    propertiitems=Property_detail.objects.all()
    form = propertydetailform(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = propertydetailform()
    context = {
        'property':form,
        'propertiitems':propertiitems
    }
    return render(request, 'myadmin/addproperty.html', context)

def readme_form(request):
    readmeitems=Readme.objects.all()
    form = readmeform(request.POST or None)
    if form.is_valid():
        form.save()
        form = readmeform()
    context = {
        'readme':form,
        'readmeitems':readmeitems
    }
    return render(request, 'myadmin/addreadme.html', context)

def agent_form(request):
    agentitems=Agentdetail.objects.all()
    form = agentform(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = agentform()
    context = {
        'agent':form,
        'agentitems':agentitems
    }
    return render(request, 'myadmin/addagents.html', context)

def comment_form(request):
    items =Comment.objects.all()
    form = commentform(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = commentform()
    context = {
        'comment':form,
        'items':items
    }
    return render(request, 'myadmin/addcomment.html', context)


def selled_form(request):
    form = selledform(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        form = selledform()
    context = {
        'selled':form
    }
    return render(request, 'myadmin/selledproperty.html', context)

def rental_form(request):
    form = rentalform(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        form = rentalform()
    context = {
        'rental':form
    }
    return render(request, 'myadmin/rentalpro.html', context)

def appointemnt_form(request):
    appoitems=Apointment.objects.all()
    form = appointemntform(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        form = appointemntform()
    context = {
        'appointment':form,
        'appoitems':appoitems

    }
    return render(request, 'myadmin/appointment.html', context)

def loginview(request):
    return render(request, "myadmin/login.html")


def registerview(request):
    if request.method =='POST':
        name =request.POST["username"]
        # emaill=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
           user =User.objects.create_user(username=name,password1=password1,password2=password2)
           user.save()
           messages.warning(request,'Successfully created')
           return redirect( 'myadmin:login_urls')
        
        else:
            messages.warning(request,'mismatch')
            return redirect('myadmin:register_urls')
    
    else:
        form = UserCreationForm()
        return render(request, "myadmin/register.html",{'form':form})


def deleteservice(request, pk):
    ser=Services.objects.get(id=pk)
    if request.method=='POST':
        ser.delete()
        return redirect ('service_urls')
    context = {
         'ser':ser
    }
    return render(request,'servicedelete.html',context)
















# def post5(self, request, *args, **kwargs):
#         if request.method =='POST':
#             form5 = self.form_class3(request.POST)in request.FILES and request.FILES['file']
#             if form5.is_valid():
#              form5.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form5": form5})
     
# def post6(self, request, *args, **kwargs):
#         if request.method =='POST':
#            form6 = self.form_class6(request.POST)in request.FILES and request.FILES['file']
#            if form6.is_valid():
#              form6.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form6": form6})
     
# def post7(self, request, *args, **kwargs):
#         if request.method =='POST':
#            form7 = self.form_class7(request.POST)in request.FILES and request.FILES['file']
#            if form7.is_valid():
#              form7.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form7": form7})
     
# def post8(self, request, *args, **kwargs):
#         if request.method =='POST':
#            form8 = self.form_class8(request.POST)in request.FILES and request.FILES['file']
#            if form8.is_valid():
#              form8.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form8": form8})
     
# def post9(self, request, *args, **kwargs):
#         if request.method =='POST':
#            form9 = self.form_class9(request.POST)in request.FILES and request.FILES['file']
#            if form9.is_valid():
#              form9.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form9": form9})
     
# def post10(self, request, *args, **kwargs):
#         if request.method =='POST':
#            form10 = self.form_class10(request.POST)in request.FILES and request.FILES['file']
#            if form10.is_valid():
#              form10.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form10": form10})
     
# def post11(self, request, *args, **kwargs):
#         if request.method =='POST':
#            form11 = self.form_class11(request.POST)in request.FILES and request.FILES['file']
#            if form11.is_valid():
#              form11.save()
#             # <process form cleaned data>
#              return redirect('admin1')

#         return render(request, self.template_name, {"form11": form11})
     

     