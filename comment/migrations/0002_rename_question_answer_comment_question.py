# Generated by Django 3.2.6 on 2021-08-12 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='question_answer',
            new_name='question',
        ),
    ]