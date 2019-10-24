from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item, FavoriteItem

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User	
		fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
			view_name='api-item-detail',
			lookup_field='id',
			lookup_url_kwarg='item_id'
		)

	#added_by = serializers.SerializerMethodField()
	added_by = UserSerializer() # the field name 'added_by' has to match the field name in the model for it to be auto detected as a User object
	total_favs = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['id', 'name', 'description', 'added_by', 'total_favs','detail']

	# this is not needed when feeding the object directly to the serializer as it matches the field name in the model
	#def get_added_by(self, object):
	#	return UserSerializer(instance=object.added_by, read_only=True).data

	def get_total_favs(self, object):
		return FavoriteItem.objects.filter(item=object).count()


class ItemDetailsSerializer(serializers.ModelSerializer):
	fav_users = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['id', 'name', 'description', 'image', 'fav_users']

	def get_fav_users(self, object):
		#users = FavoriteItem.objects.filter(item=object).distinct().values('user')
		#print(users)
		favs = object.favoriteitem_set.all()
		users = []

		for fav in favs:
			users.append(fav.user)

		#user_list = []
		#for user in users:
		#	user_list.append(UserSerializer(instance=User.objects.get(id=user["user"])).data)

		#print(user_list)

		#return user_list

		return UserSerializer(users, many=True).data

