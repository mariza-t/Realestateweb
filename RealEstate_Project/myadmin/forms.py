from django import forms
from RealEstate_App.models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

    
class readmeform(forms.Form):
    title =forms.CharField(max_length=60)
    readme = forms.CharField(label='Description',widget=forms.Textarea)

class readmeform(forms.ModelForm):  
    class Meta:  
        model = Readme
        fields = "__all__"
    def str(self) -> str:
            return self.title
    
class agentform(forms.Form):
    name = forms.CharField(max_length=50)
    discription = forms.CharField(label='Description',widget=forms.Textarea)
    image = forms.ImageField() 

class agentform(forms.ModelForm):  
    class Meta:  
        model = Agentdetail
        fields =  "__all__"
    def str(self) -> str:
            return self.name
    
    
class commentform(forms.Form):
    flname = forms.CharField(max_length=50)
    qoutetitle = forms.CharField(max_length=50)
    comment= forms.CharField(label='Description',widget=forms.Textarea)
    profession = forms.CharField(max_length=50)
    photo = forms.ImageField()

class commentform(forms.ModelForm):  
    class Meta:  
        model = Comment
        fields =  "__all__"
    def str(self) -> str:
            return self.flname
    



class serviceform(forms.Form):
    service_title = forms.CharField(max_length=50)
    services_discription = forms.CharField(label='Description',widget=forms.Textarea)

class serviceform(forms.ModelForm):  
    class Meta:  
        model = Services
        fields =  "__all__"
    def str(self) -> str:
            return self.service_title
    

# on gallery 
class galleryform(forms.Form):
    imgname = forms.CharField(max_length=50)
    pictures = forms.ImageField()

class galleryform(forms.ModelForm):  
    class Meta:  
        model = Gallery
        fields =  "__all__"
    
    def str(self) -> str:
            return self.imgname


class propertydetailform(forms.Form):
    images= forms.ImageField()
    hometype= forms.CharField(max_length=80)
    homediscription =forms.CharField(label='Description',widget=forms.Textarea)
    Address = forms.CharField(label='Description',widget=forms.Textarea)
    postedby = forms.CharField(max_length=50)
    date = forms.DateField()
    price_space = forms.IntegerField()

class propertydetailform(forms.ModelForm):  
    class Meta:  
        model = Property_detail
        fields =  "__all__"
    def str(self) -> str:
            return self.hometype
    

class contactform(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    comments = forms.CharField(label='Description',widget=forms.Textarea)
class contactform(forms.ModelForm):  
    class Meta:  
        model = Request_for_Contact
        fields = "__all__"
        
    def str(self) -> str:
            return self.title

class appointemntform(forms.Form):
    first_name1 = forms.CharField(max_length=50)
    last_name1 = forms.CharField(max_length=50)
    email1 = forms.EmailField()
    phone1 = forms.IntegerField()
 

class appointemntform(forms.ModelForm):  
    class Meta:  
        model = Apointment
        fields =  "__all__"
    
    def str(self) -> str:
            return self.title

# on admin


    

class selledform(forms.Form):
    selledpro_no = forms.IntegerField()
    Properties=forms.ModelChoiceField(queryset=Property_detail.objects.all())

class selledform(forms.ModelForm):  
    class Meta:  
        model = Selledproperty
        fields =  "__all__"
    def str(self) -> str:
            return self.selledpro_no
    
class rentalform(forms.Form):
    properties=forms.ModelChoiceField(queryset=Property_detail.objects.all())
    availablefrom =forms.DateTimeField()
    remain_amount = forms.IntegerField()
    nextpayment = forms.ImageField()
    nextpaymentduration =forms.DurationField()

    class rentalform(forms.ModelForm):  
        class Meta:  
            model = Rentelproperty
            fields =  "__all__"
    def str(self) -> str:
            return self.properties
    

class customerform(forms.Form):
    name = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Phoneno = forms.IntegerField()
    Address= forms.CharField(max_length=100)

class customerform(forms.ModelForm):  
    class Meta:  
        model = Cutsomer
        fields =  "__all__"
    
class CreateUserForm(UserCreationForm):
     class Meta:
          model=User
          fields =['username','password1','password2']
