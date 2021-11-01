# Generated by Django 3.2.8 on 2021-11-01 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inform', '0009_auto_20211101_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='occupant', to='inform.neighbourhood'),
        ),
    ]
