# Generated by Django 3.2.6 on 2021-08-12 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question_answer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('added_date', models.DateTimeField()),
                ('question_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_answer.question')),
            ],
        ),
    ]
