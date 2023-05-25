# Generated by Django 4.2.1 on 2023-05-23 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_galleryimage_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlansFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('pricing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.subscriptionplans')),
            ],
        ),
    ]