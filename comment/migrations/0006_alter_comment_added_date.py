# Generated by Django 3.2.6 on 2021-09-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_alter_comment_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='added_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]