# Generated by Django 2.1.3 on 2018-12-10 07:13

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mongos', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListEntry',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=255)),
                ('authors', djongo.models.fields.ListField()),
            ],
        ),
    ]
