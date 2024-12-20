# Generated by Django 5.1.3 on 2024-11-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GustoHelado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='gustos/')),
                ('categoria', models.CharField(choices=[('crema', 'Crema'), ('frutal', 'Frutal')], default='crema', max_length=50)),
            ],
        ),
    ]
