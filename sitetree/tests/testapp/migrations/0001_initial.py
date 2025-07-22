# Generated migration for testapp

from django.db import migrations, models


class Migration(migrations.Migration):
    
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afield', models.CharField(max_length=20, verbose_name='my')),
            ],
        ),
    ] 