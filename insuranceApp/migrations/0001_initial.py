# Generated by Django 3.2.2 on 2021-06-06 02:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('description', models.TextField()),
                ('read', models.BooleanField(blank=True, default=False, null=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('uz', 'uz'), ('oz', 'oz'), ('ru', 'ru'), ('en', 'en')], max_length=255, null=True)),
                ('region', models.IntegerField(choices=[(1, 'Toshkent shahri'), (2, 'Toshkent viloyati'), (3, 'Sirdaryo viloyati'), (4, 'Jizzax viloyati'), (5, 'Samarqand viloyati'), (6, 'Qashqadaryo viloyati'), (7, 'Surxondaryo viloyati'), (8, 'Buxoro viloyati'), (9, 'Navoiy viloyati'), (10, 'Xorazm viloyati'), (11, 'Andijon viloyati'), (12, "Farg'ona viloyati"), (13, 'Namangan viloyati'), (14, "Qoraqalpog'iston Respublikasi")])),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('workDate', models.CharField(max_length=500)),
                ('workClock', models.CharField(max_length=255)),
                ('mapLocation', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('uz', 'uz'), ('oz', 'oz'), ('ru', 'ru'), ('en', 'en')], max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('postImage', models.ImageField(blank=True, upload_to='post')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, upload_to='servis-classes')),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
