from rest_framework import serializers
from StockAPI.models import Item,Unit,Transaction


class UnitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Unit
		fields = ('name', 'shorthand')

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction


class ItemSerializer(serializers.ModelSerializer):
	itemUnit = serializers.RelatedField(many=False)#RelatedField is used to represent the target of the relationship using its __unicode__ method
	itemTransaction = serializers.RelatedField(many=True)
	# check 	HyperlinkedRelatedField is used to represent the target of the relationship using a hyperlink
		
	class Meta:
		model = Item
		fields=('item_id','item_name','item_unit','quantity','balance','timestamp','itemUnit','itemTransaction')
		


			



					