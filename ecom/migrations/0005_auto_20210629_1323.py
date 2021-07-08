# Generated by Django 2.2.10 on 2021-06-29 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_auto_20210629_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Product'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NombreProducto',
        ),
    ]
