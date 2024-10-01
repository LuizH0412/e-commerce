# Generated by Django 5.1 on 2024-09-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Pago', 'Pago'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=200, verbose_name='Status do Pedido'),
        ),
    ]