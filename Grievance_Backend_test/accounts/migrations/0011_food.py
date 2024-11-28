# Generated by Django 4.2.7 on 2024-05-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=15)),
                ('batch', models.CharField(max_length=15)),
                ('phone_no', models.IntegerField()),
                ('data', models.TextField()),
                ('importance', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High'), (5, 'Critical')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
            ],
        ),
    ]
