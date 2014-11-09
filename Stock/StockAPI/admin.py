from django.contrib import admin
from StockAPI.models import Item,Unit,Transaction

# Register your models here.
class UnitAdmin(admin.ModelAdmin):
	list_display = ('name','shorthand')

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Item Details',               {'fields': ['item_id','item_name','item_unit','quantity','balance']}),
        ('Date information', {'fields': ['timestamp']}),
    ]
    list_display = ('item_name','item_unit', 'quantity','balance')

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction Details',               {'fields': ['item','transaction_type','quantity','cost','inventory','date','consumption']}),
        ('Date information', {'fields': ['timestamp']}),
        ('Comments', {'fields': ['comments']}),
    ]
    list_display = ('item','quantity', 'inventory','timestamp')
    list_filter=['timestamp'] #date_hierarchy : another way 
    search_fields=['item'] #ordering 
    # filter_horizontal : check ! works on many to many fields
    # raw_id_fields : check!

admin.site.register(Item,ItemAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(Transaction,TransactionAdmin)