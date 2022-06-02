from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Category(models.Model):
  cat_product = [
    ('hot','hot'),
    ('new','new'),
    ('sale','sale'),
  ]
  name = models.CharField(max_length=50, null=True, blank=True, choices=cat_product)
  def __str__(self):
    return self.name

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=100, null=True)
  email = models.EmailField(max_length=254, null=True)
  def __str__(self):
    return self.name
  
  
class Colors(models.Model):
  colors = [
    ('red','red'),
    ('green','green'),
    ('blue','blue'),
    ('yellow','yellow'),
    ('orange','orange'),
    ('pink','pink'),
  ]
  name = models.CharField(max_length=50, null=True, blank=True, choices=colors) 
  def __str__(self):
    return self.name


class Size(models.Model):
  sizes = [
    ('small','small'),
    ('larg','larg'),
    ('medium','medium'),
    ('xl','xl'),
    ('2xl','2xl'),
    ('big','big'),
  ]
  size = models.CharField(max_length=50, null=True, blank=True, choices=sizes) 
  def __str__(self):
    return self.size
   
  
class Product(models.Model):
  title = models.CharField(max_length=50, null=True, blank=True)
  price = models.DecimalField(max_digits=5,decimal_places=2 ,null=True, blank=True)
  rrp = models.DecimalField(max_digits=5,decimal_places=2 ,null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  productimage = models.ImageField(upload_to="photos/%y/%m/%d", null=True, blank=True)
  colors = models.ForeignKey(Colors, on_delete=models.PROTECT, max_length=50, null=True, blank=True)
  sizes = models.ForeignKey(Size, on_delete=models.PROTECT, null=True, blank=True)
  image1 = models.ImageField(null=True, blank=True)
  image2 = models.ImageField(null=True, blank=True)
  image3 = models.ImageField(null=True, blank=True)
  image4 = models.ImageField(null=True, blank=True)
  image5 = models.ImageField(null=True, blank=True)
  is_active = models.BooleanField(default=True)
  date_added = models.DateTimeField(auto_created=True, null=True, blank=True)
  
  class Meta:
    ordering = ['-date_added']
  def __str__(self):
    return self.title
    
    
class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  date_ordered = models.DateTimeField(auto_now_add=True)
  complate = models.BooleanField(default=False, null=True, blank=False)
  transaction_id = models.CharField(max_length=200, null=True)
  def __str__(self):
    return str(self.id)
  
class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class ShippingAdress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
  adress = models.CharField(max_length=200, null=True)
  adress2 = models.CharField(max_length=200, null=True)
  zipcode = models.CharField(max_length=200, null=True)
  country = CountryField(blank_label='(select country)', null=False, blank=False)
  # phone = models.PhoneNumberField(null=True, blank=True)
  email = models.EmailField(max_length=50 ,null=True, blank=True)
  terms_conditions = models.BooleanField(default=False, null=True, blank=False)
  save_information = models.BooleanField(default=False, null=True, blank=False)
  subscribe = models.BooleanField(default=False, null=True, blank=False)
  pyment = models.BooleanField(default=False, null=False, blank=False)
  date_added = models.DateTimeField(auto_now_add=True, null=False, blank=False)
  
  def __str__(self):
    return self.adress
  
  
class Blog(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  blog_image = models.ImageField(null=True, blank=True)
  posted_date = models.DateTimeField(auto_created=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  blog_post = models.TextField(max_length=5000, null=True, blank=True)
  def __str__(self):
    return self.title
  
  @property
  def blogURL(self):
    try:
      blo = self.blog_image
    except:
      blo = ""
    return blo