from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE )
    name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100, null=True)
    def __str__(self):
        return self.name
    
class s_and_t(models.Model):
    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField(null= True, blank=True, upload_to ='images/')
    description= models.CharField(max_length = 500)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    links= models.URLField(max_length = 500)
    verified= models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url =self.thumbnail.url
        except:
            url= ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered =models.BooleanField(default=False)
    transact_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
        
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems= self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    S_and_t = models.ForeignKey(s_and_t, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.S_and_t.price * self.quantity
        return total
    

class Category(models.Model):
    tag= models.CharField(max_length=250)
    def __str__(self):
        return self.tag

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publish_date= models.DateField(default= 2022-11-22)
    what = models.TextField(max_length = 2500)
    what_img = models.ImageField(null= True, blank=True,  upload_to ='images/')
    how = models.TextField(max_length = 2500)
    how_img= models.ImageField(null= True,  blank=True, upload_to ='images/')
    why = models.TextField(max_length = 2500)
    why_img= models.ImageField(null= True,  blank=True,upload_to ='images/')
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title













