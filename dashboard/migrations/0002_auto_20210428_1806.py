# Generated by Django 3.1.7 on 2021-04-28 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='penshifts',
            name='employee_Number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='penshifts',
            name='shift_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.avlshifts'),
        ),
        migrations.AddField(
            model_name='avlshifts',
            name='store_Number',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.stores'),
        ),
    ]
