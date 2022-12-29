from rest_framework import serializers
from .models import Payment, Payments_expired

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    
    def validate(self, data):
        amount = data.get('amount')
        if amount < 0:
            raise serializers.ValidationError('El monto no puede ser negativo')
        return data
    
class PaymentExpiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments_expired
        fields = '__all__'
        