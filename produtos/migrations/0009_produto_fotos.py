# Generated by Django 5.1 on 2024-10-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_remove_produto_fotos_alter_produto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Fotos'),
        ),
    ]
