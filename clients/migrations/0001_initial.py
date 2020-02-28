# Generated by Django 2.0 on 2020-02-25 14:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('credit_purpose', models.CharField(max_length=100)),
                ('credit_amount', models.CharField(max_length=100)),
                ('collateral', models.CharField(max_length=200)),
                ('credit_history', models.CharField(max_length=200)),
                ('finan_perfor', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('state', models.BooleanField(default=0)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('spouse_name', models.CharField(max_length=100)),
                ('dependant', models.CharField(max_length=100)),
                ('birth_date', models.CharField(max_length=100)),
                ('birth_palce', models.CharField(max_length=100)),
                ('passport_no', models.CharField(max_length=100)),
                ('issued_by', models.CharField(max_length=100)),
                ('issued_date', models.CharField(max_length=100)),
                ('register_place', models.CharField(max_length=100)),
                ('residential_add', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('inn', models.CharField(max_length=100)),
                ('contacts', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_activity', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('employee_num', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('password', models.CharField(default=None, max_length=128, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Collateral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('market_value', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='credit_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_loan', models.CharField(max_length=100)),
                ('credit_amount', models.CharField(max_length=100)),
                ('period', models.DateTimeField()),
                ('goal', models.CharField(max_length=100)),
                ('contribution_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.PositiveIntegerField()),
                ('applicant', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('market_value', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_activity', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('documents', models.FileField(blank=True, default='/media/index.jpeg', upload_to='media/clients')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
        migrations.AddField(
            model_name='applyclient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
    ]
