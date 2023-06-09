# Generated by Django 4.2.1 on 2023-05-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_rename_inquery_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='gallery/')),
            ],
            options={
                'verbose_name_plural': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(max_length=150)),
                ('img', models.ImageField(null=True, upload_to='gallery_imgs/')),
            ],
        ),
    ]
