# Generated by Django 2.2.3 on 2020-04-15 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200414_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='level',
        ),
        migrations.AddField(
            model_name='member',
            name='level0',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='member',
            name='upLevel_id',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
