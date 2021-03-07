# api-small-business/stores/models.py
from django.db import models
from django.core.validators import MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return "{}".format(self.name)
    

class District(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return "{}".format(self.name)
    
    
class PointOfSale(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=12)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    
    def __str__(self) -> str:
        return "{}".format(self.name)
    
    
class Seller(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    seller_id = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)   
    

class Product(models.Model):
    name = models.CharField(max_length=80)
    reference = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return "{}".format(self.name)
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=12)
    district = models.ForeignKey(District,
                                 on_delete=models.CASCADE,
                                 related_name='districts')
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE,
                             related_name='cities'
                             )
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name='customers',
                                 help_text='Select customer')
    date = models.DateField(help_text='Add order date')
    
    def __str__(self) -> str:
        return "{}".format(self.customer)


class OrderDetail(models.Model):
    class PaymentsMethod(models.TextChoices):
        NONE = "undefined", "Undefined",
        CASH = "cash", "Cash",
        CHECKS = "checks", "Checks",
        DEBIT_CARDS = "debit_cards", "Debit cards",
        CREDIT_CARDS = "credit_cards", "Credit cards",
        MOBILE_PAYMENTS = "mobile_payments", "Mobile payments",
        BANK_TRANSFERS = "bank_transfers", "Bank transfers",
        
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='products',
                              help_text='Select order by customer')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='orders',
                                help_text='Select purchased product')
    payment = models.CharField('Payments Method',
                            max_length=20,
                            choices=PaymentsMethod.choices,
                            default=PaymentsMethod.NONE)
    seller = models.ForeignKey(Seller, 
                                  on_delete=models.CASCADE,
                                  related_name='sellers')
    location = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "{}".format(self.order)