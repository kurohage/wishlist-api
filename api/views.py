from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User

from .models import Item, FavoriteItem
from .serializers import ItemListSerializer, ItemDetailsSerializer
from .permissions import IsItemOwner

# Create your views here.
class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = '__all__'

class ItemDetailsView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	permission_classes = [IsAuthenticated, IsItemOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
