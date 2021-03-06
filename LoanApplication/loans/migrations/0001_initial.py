# Generated by Django 2.2.2 on 2019-08-03 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestedLoanAmount', models.FloatField(default=0)),
                ('StatedCreditHistory', models.IntegerField(default=0)),
                ('LegalEntityType', models.CharField(max_length=20)),
                ('FilterID', models.IntegerField(default=0)),
                ('CFRequestId', models.IntegerField(default=0)),
                ('RequestDate', models.DateTimeField()),
                ('CFApiUserId', models.IntegerField(default=0, null=True)),
                ('CFApiPassword', models.CharField(max_length=100, null=True)),
                ('IsTestLead', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('AnnualRevenue', models.FloatField(default=0)),
                ('MonthlyAverageBankBalance', models.FloatField(default=0)),
                ('MonthlyAverageCreditCardVolume', models.FloatField(default=0)),
                ('TaxID', models.CharField(max_length=10)),
                ('Phone', models.CharField(max_length=20)),
                ('NAICS', models.CharField(max_length=5)),
                ('HasBeenProfitable', models.BooleanField(default=False)),
                ('HasBankruptedInLast7Years', models.BooleanField(default=False)),
                ('InceptionDate', models.DateTimeField()),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200, null=True)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=20)),
                ('Zip', models.CharField(max_length=5)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('App', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app', to='loans.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateTimeField()),
                ('SSN', models.CharField(max_length=9)),
                ('PercentageOfOwnership', models.FloatField(default=0)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200, null=True)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=20)),
                ('Zip', models.CharField(max_length=5)),
                ('HomePhone', models.CharField(max_length=20, null=True)),
                ('Business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Owners', to='loans.Business')),
            ],
        ),
    ]
