# Generated by Django 2.0 on 2020-02-17 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0008_auto_20200216_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedfile',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='managers.Bank'),
        ),
    ]
