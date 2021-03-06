# Generated by Django 2.2.1 on 2019-06-07 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20190606_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentsmodel',
            options={'ordering': ('-posted_on',)},
        ),
        migrations.AddField(
            model_name='commentsmodel',
            name='name',
            field=models.CharField(default='anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='commentsmodel',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentsmodel',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
