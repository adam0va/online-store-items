# Generated by Django 2.2.13 on 2020-07-02 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_app', '0007_auto_20200625_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
