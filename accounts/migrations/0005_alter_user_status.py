# Generated by Django 3.2.3 on 2021-06-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_available_bal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Dormant', 'Dormant'), ('Deactivated', 'Deactivated')], default='Active', max_length=11, null=True),
        ),
    ]
