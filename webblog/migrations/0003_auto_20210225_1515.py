# Generated by Django 3.1.7 on 2021-02-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0002_auto_20210225_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('blog', models.CharField(max_length=500)),
                ('privacy', models.BooleanField(default=False)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='usersinfo',
            name='images',
        ),
    ]
