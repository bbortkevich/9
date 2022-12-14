# Generated by Django 4.1.2 on 2022-10-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(db_column='rating', default=0),
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='rating',
            new_name='comment_rating',
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(db_column='rating', default=0),
        ),
        migrations.RenameField(
            model_name='post',
            old_name='rating',
            new_name='post_rating',
        ),
    ]
