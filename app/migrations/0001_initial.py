# Generated by Django 3.2.4 on 2021-06-14 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('ANI', 'andaman & nicobar islands'), ('andhra p', 'andhra pradesh'), ('arunachal p', 'arunachal pradesh'), ('ass', 'assam'), ('bih', 'bihar'), ('chat', 'chandigarah'), ('chandi', 'chhatisgarah'), ('dadarNagar', 'dadar & nagar haveli'), ('dlh', 'delhi'), ('goaa', 'goa'), ('guj', 'gujrat'), ('har', 'haryana'), ('him p', 'himachal pradesh'), ('J&K', 'jammu & kashmir'), ('jhar', 'jharkhand'), ('kar', 'karnataka'), ('ker', 'kerla'), ('laksh', 'lakshadweep'), ('MP', 'madhya pradesh'), ('maha', 'maharashtra'), ('Mani', 'manipur'), ('Megh', 'meghalay'), ('Mizz', 'mizoram'), ('naga', 'nagaland'), ('odi', 'odisha'), ('podu', 'poducherry'), ('pun', 'punjab'), ('rat', 'rajasthan'), ('sik', 'sikkim'), ('tam', 'tamil nadu'), ('tel', 'telangana'), ('tri', 'tripura'), ('uttra', 'uttrakhand'), ('UP', 'uttar pradesh'), ('WB', 'west bengal')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=8)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Acc', 'accepted'), ('Pac', 'packed'), ('OnWay', 'on the way'), ('Del', 'delivered'), ('Can', 'cancel')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]