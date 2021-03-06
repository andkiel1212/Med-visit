# Generated by Django 4.0.1 on 2022-02-14 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_patient', models.CharField(max_length=100)),
                ('surname_patient', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visit', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('recommendation_visit', models.TextField()),
                ('create_visit', models.DateTimeField(auto_now_add=True)),
                ('execute_visit', models.CharField(choices=[('yes', 'TAK'), ('no', 'NIE')], default='yes', max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit', to='patient.patient')),
            ],
            options={
                'ordering': ('create_visit',),
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_parent', models.CharField(max_length=20)),
                ('surname_parent', models.CharField(max_length=20)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='patient.patient')),
            ],
        ),
    ]
