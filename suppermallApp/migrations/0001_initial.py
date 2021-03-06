# Generated by Django 2.2 on 2020-07-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GoodsName', models.CharField(max_length=100, null=True)),
                ('GoodsPhoto', models.ImageField(blank=True, null=True, upload_to='GoodsPhoto')),
                ('GoodsPrice', models.FloatField(max_length=50)),
                ('Page', models.SmallIntegerField()),
                ('CollectionCount', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
