# Generated by Django 4.2.1 on 2023-05-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0012_subscriptionplans_highlight_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionplansfeature',
            name='pricing',
        ),
        migrations.AddField(
            model_name='subscriptionplansfeature',
            name='pricing',
            field=models.ManyToManyField(to='gym.subscriptionplans'),
        ),
    ]