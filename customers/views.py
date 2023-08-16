from customers.models import Customer
from django.http.response import JsonResponse
from customers.serializers import CustomerSerializer  

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)  
    return JsonResponse({'customers': serializer.data})



def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})
