from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item, FavoriteItem

class ItemSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
			view_name='api-item-detail',
			lookup_field='id',
			lookup_url_kwarg='item_id'
		)

	class Meta:
		model = Item
		fields = ['id', 'name', 'description', 'detail']


class ItemDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ['name', 'description', 'image', 'id']