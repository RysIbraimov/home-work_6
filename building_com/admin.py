from django.contrib import admin
from .models import Block,Clients
# Register your models here.

@admin.register(Clients)
class AdminClients(admin.ModelAdmin):
    date_hierarchy = 'sale_date'
    search_fields = ('name',)
    list_display = ('name','sale_date','status','total_area','total_area_price')
    empty_value_display = '--без хоз --'

    @admin.display(description='Общая стоимость')
    def total_area_price(self,obj):
        return f'{obj.total_area * obj.block.kv_metr_price}$'

@admin.register(Block)
class AdminBlock(admin.ModelAdmin):
     list_display = ('block_number','entrance_count','apartment_per_floor','floor','total_apartments')

     def total_apartments(self,obj):
         return f'{obj.floor * obj.apartment_per_floor} квартир'