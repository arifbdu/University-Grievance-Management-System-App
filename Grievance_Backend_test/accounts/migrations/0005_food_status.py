# Generated by Django 4.2.7 on 2024-05-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_authority_certificate_food_hostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='status',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
