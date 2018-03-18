# Generated by Django 2.0.3 on 2018-03-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_cate_isdel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='', max_length=100)),
                ('info', models.CharField(default='', max_length=300)),
                ('thumb', models.ImageField(upload_to='thumb')),
                ('content', models.TextField(default='')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('isDel', models.BooleanField(default=False)),
                ('cateId', models.IntegerField(default=0)),
            ],
        ),
    ]
