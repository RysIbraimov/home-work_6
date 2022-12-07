from django.db import models

# Create your models here.
class Block(models.Model):
    block_number = models.IntegerField()
    kv_metr_price = models.IntegerField()
    entrance_count = models.IntegerField()
    floor = models.IntegerField(default=7)
    apartment_per_floor = models.IntegerField()



class Clients(models.Model):
    name = models.CharField(max_length=20,verbose_name='ФИО', null=True,blank=True)
    sale_date = models.DateField(null=True,blank=True)
    block = models.ForeignKey(Block,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=(
        ('Выкуп','выкуп'),
        ('Выкуп не до конца','Выкуп не до конца'),
        ('Расторгнуто','Расторгнуто'),
        ('Не продано','Не продано'),
    ))
    total_area = models.IntegerField()

    def __str__(self):
        return self.name

