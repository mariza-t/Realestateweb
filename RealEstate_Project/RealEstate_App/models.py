from django.db import models

# on home page 
    
class Readme(models.Model):
    title =models.CharField(max_length=60)
    readme = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.title
    
class Agentdetail(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(max_length=250)
    image = models.ImageField()


    def __str__(self) -> str:
        return self.name
    
class Comment(models.Model):
    flname = models.CharField(max_length=50)
    qoutetitle = models.CharField(max_length=50)
    comment= models.TextField(max_length=150)
    profession = models.CharField(max_length=50)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.flname
    

# on services  

class Services(models.Model):
    service_title = models.CharField(max_length=50)
    services_discription = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.service_title


    

# on gallery 
class Gallery(models.Model):
    imgname = models.CharField(max_length=50)
    pictures = models.ImageField()

    def __str__(self) -> str:
        return self.imgname

    

# on properties detail

class Property_detail(models.Model):
    images= models.ImageField()
    hometype= models.CharField(max_length=80)
    homediscription =models.TextField(max_length=180)
    Address = models.TextField(max_length=100)
    postedby = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    price_space = models.IntegerField()

    def __str__(self) -> str:
        return self.hometype

    
    
# on contact  form
class Request_for_Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    comments = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.first_name + self.last_name

# appointment
class Apointment(models.Model):
    first_name1 = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    email1 = models.EmailField()
    phone1 = models.IntegerField()


    def __str__(self) -> str:
        return self.first_name1 + self.last_name1 
    
    

# on admin

class Selledproperty(models.Model):
    selledpro_no = models.IntegerField()
    Properties=models.ForeignKey("Property_detail", on_delete=models.SET_NULL, null=True)

    def str(self) -> str:
        return self.selledpro_no
    
class Rentelproperty(models.Model):
    Properties=models.ForeignKey("Property_detail", on_delete=models.SET_NULL, null=True)
    availablefrom =models.DateTimeField()
    remain_amount = models.IntegerField()
    nextpayment = models.ImageField()
    nextpaymentduration =models.DurationField()

    def str(self) -> str:
        return self.propertyname
    
class Cutsomer(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phoneno = models.IntegerField()
    Address= models.CharField(max_length=100)

    def str(self) -> str:
        return self.name
    