# Generated by Django 4.1.5 on 2023-01-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_delete_decretopresidencial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecretoPresidencial',
            fields=[
                ('lei', models.TextField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('ementa', models.TextField()),
                ('inteiroTeor', models.TextField()),
            ],
        ),
    ]
