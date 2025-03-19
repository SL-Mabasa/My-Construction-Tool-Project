from django.db import models
import datetime

# Create your models here.


# Ecommerce 'Service Action VO' Details
class action(models.Model):
    type = models.CharField(max_length= 100)
    description = models.CharField(max_length=100)
    quote = models.IntegerField
    profit = models.IntegerField
    rate = models.IntegerField
    qty = models.IntegerField
    unit = models.CharField(max_length=100)
    amount = models.IntegerField
    
    '''rate = quote + (profit * quote)
    amount = qty * rate'''
    
    def __str__(self):
        '''info_1= f'{self.description}\n{self.quote}\n{self.profit}\n{self.rate}'
        info_2 = f'\n{self.qty}\n{self.unit}\{self.amount}'
        info = info_1 + info_2'''
        return self.type

# Ecommerce Service type fee
'''class prices(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.ForeignKey(action, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.price'''

# Ecommerce Customer Details
class customers(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=12)
    
    def __str__(self):
        return self.email
    
# E-Commerce Category Product   
class category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# E-Commerce Product
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default = 0, decimal_places=2, max_digits=9) 
    description = models.CharField(max_length=250, default='', blank=True, null= True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')
    def __str__(self):
        return self.name

# E-Commerce Order
class order(models.Model):
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default = '', blank= True)
    phone = models.CharField(max_length=10, default='', blank=True)
    status = models.BooleanField(default=False)
    total = models.IntegerField
    date_created = models.DateTimeField(default = datetime.datetime.now)
    def __str__(self):
        return self.product