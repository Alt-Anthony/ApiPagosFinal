from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment,Payments_expired
from .serializers import PaymentSerializer, PaymentExpiredSerializer
from rest_framework.response import Response
from rest_framework import status
from .pagination import Pagination

class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = Pagination
    
    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payment_date = serializer.data.get('payment_date') 
            expiraton_date = serializer.data.get('expiration_date')
            if expiraton_date < payment_date:
                record = {
                    "amount_fee": 0.2*float(serializer.data.get('amount')),
                    "payment_id": serializer.data.get('id'),
                    "amount": serializer.data.get('amount'),
                    "service_id": serializer.data.get('service_id'),
                    "user_id": serializer.data.get('user_id')         
                }
                serializer2 = PaymentExpiredSerializer(data=record)
                if serializer2.is_valid():
                    serializer2.save()
                    return Response({
                        "ok":True,
                        "message": "Añadido a la lista",
                        "data 1": serializer.data,
                        "message": "Añadido en la lista de pagos expirados",
                        "data 2": serializer2.data
                    }, status=status.HTTP_201_CREATED)
            return Response({
                "ok":True,
                "message": "Añadido",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class PaymentExpiredView(viewsets.ModelViewSet):
    queryset = Payments_expired.objects.all()
    serializer_class = PaymentExpiredSerializer
