# Generated by Django 4.2.7 on 2024-05-17 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=15)),
                ('batch', models.CharField(max_length=15)),
                ('room_no', models.IntegerField()),
                ('data', models.TextField()),
                ('importance', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High'), (5, 'Critical')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=15)),
                ('batch', models.CharField(max_length=15)),
                ('room_no', models.IntegerField()),
                ('data', models.TextField()),
                ('importance', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High'), (5, 'Critical')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=15)),
                ('batch', models.CharField(max_length=15)),
                ('room_no', models.IntegerField()),
                ('data', models.TextField()),
                ('importance', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High'), (5, 'Critical')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=15)),
                ('batch', models.CharField(max_length=15)),
                ('room_no', models.IntegerField()),
                ('data', models.TextField()),
                ('importance', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High'), (5, 'Critical')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]