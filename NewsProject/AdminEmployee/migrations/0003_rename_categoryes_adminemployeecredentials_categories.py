# Generated by Django 5.1.4 on 2024-12-07 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminEmployee', '0002_categories_adminemployeecredentials_categoryes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminemployeecredentials',
            old_name='categoryes',
            new_name='categories',
        ),
    ]
