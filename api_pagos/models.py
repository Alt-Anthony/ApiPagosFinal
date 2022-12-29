from django.db import models
from django.contrib.auth.models import User
from api_servicios.models import Service



class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    expiration_date = models.DateField()
    
    class Meta:
        db_table = 'Api_Pagos'
        
class Payments_expired(models.Model):
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount_fee = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'Api_Pagos_Expirados'
