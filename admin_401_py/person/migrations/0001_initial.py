# Generated by Django 4.2.2 on 2023-06-30 15:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=uuid.UUID('57640d54-175e-11ee-82bd-a675ca0253ef'), max_length=100)),
                ('name_type_document', models.CharField(max_length=100)),
                ('description_type_document', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': 'Type document',
                'verbose_name_plural': 'Types document',
            },
        ),
        migrations.CreateModel(
            name='TypePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=uuid.UUID('57641312-175e-11ee-82bd-a675ca0253ef'), max_length=100)),
                ('name_type', models.CharField(max_length=200)),
                ('description_type', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': 'Type person',
                'verbose_name_plural': 'Types person',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=uuid.UUID('576417f4-175e-11ee-82bd-a675ca0253ef'), max_length=100)),
                ('first_name_person', models.CharField(max_length=200)),
                ('last_name_person', models.CharField(max_length=200)),
                ('document_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('type_document_fk', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='person.typedocument', verbose_name='Type document')),
                ('type_person_fk', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='person.typeperson', verbose_name='Type person')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]
