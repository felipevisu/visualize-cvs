# Generated by Django 3.2.14 on 2022-12-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('academic_experience', models.TextField(blank=True)),
                ('professional_experience', models.TextField(blank=True)),
                ('instagram', models.EmailField(blank=True, max_length=200, null=True)),
                ('facebook', models.EmailField(blank=True, max_length=200, null=True)),
                ('linkedin', models.EmailField(blank=True, max_length=200, null=True)),
                ('behance', models.EmailField(blank=True, max_length=200, null=True)),
                ('portfolio_url', models.CharField(blank=True, max_length=1024, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='cvs')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('areas', models.ManyToManyField(to='jobs.Job')),
            ],
            options={
                'verbose_name': 'Currículo',
                'verbose_name_plural': 'Currículos',
                'ordering': ['-created'],
            },
        ),
    ]