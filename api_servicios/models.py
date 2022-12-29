from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.URLField(max_length=255)
    prefix = models.CharField(max_length=3, default='NoN')
    
    class Meta:
        db_table = 'Api_Servicios'
        
    def __str__(self) -> str:
        return self.name