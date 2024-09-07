# Generated by Django 5.0.6 on 2024-08-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_category_projectcategory_portfolioitem_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='categories',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='detail_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_detail_images/'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
