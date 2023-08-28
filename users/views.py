from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import Item
from .serializer import ItemSerializer


@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_data(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
