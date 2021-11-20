# Generated by Django 3.2.9 on 2021-11-18 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TanentAware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tanent')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('tanentaware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.tanentaware')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('api.tanentaware',),
        ),
    ]