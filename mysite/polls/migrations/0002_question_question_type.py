# Generated by Django 4.1.3 on 2022-12-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='polytique', max_length=100),
        ),
    ]
