# Generated by Django 3.2 on 2022-12-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_number', models.IntegerField()),
                ('kv_metr_price', models.IntegerField()),
                ('entrance_count', models.IntegerField()),
                ('apartment_per_floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='ФИО')),
                ('sale_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Выкуп', 'выкуп'), ('Выкуп не до конца', 'Выкуп не до конца'), ('Расторгнуто', 'Расторгнуто'), ('Не продано', 'Не продано')], max_length=30)),
                ('total_area', models.IntegerField()),
            ],
        ),
    ]
