from rest_framework import serializers
from reviewSystem.models import Item,Category,User,Rating
# the below line for user restriction
# from django.contrib.auth.models import User

# from django.forms import widgets ??

# class RootUserSerializer(serializers.ModelSerializer):
#     item_owner = serializers.PrimaryKeyRelatedField(many=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'item_owner')

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'items_type','item')


class ItemSerializer(serializers.ModelSerializer):
	category_type = serializers.RelatedField(many=True)
	#category_type = CategorySerializer(many=True)

	class Meta:
		model = Item
		fields = ('id', 'item_id','item_name', 'item_rating','category_type' )

class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = ('id', 'item', 'ratings', 'timestamp','user')	

class UserSerializer(serializers.ModelSerializer):
	user_rating = serializers.RelatedField(many=True)

	class Meta:
		model = User
		fields = ('id', 'user_id','first_name', 'last_name', 'email','tiemstamp','user_rating')


					