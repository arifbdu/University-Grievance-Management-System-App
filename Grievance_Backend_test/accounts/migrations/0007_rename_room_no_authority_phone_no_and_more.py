# Generated by Django 4.2.7 on 2024-05-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_authority_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authority',
            old_name='room_no',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='room_no',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='hostel',
            old_name='room_no',
            new_name='phone_no',
        ),
        migrations.AddField(
            model_name='certificate',
            name='status',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='status',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
