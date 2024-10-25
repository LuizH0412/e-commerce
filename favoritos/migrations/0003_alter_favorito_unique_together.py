# Generated by Django 5.1 on 2024-10-01 20:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favoritos', '0002_alter_favorito_usuario'),
        ('produtos', '0004_alter_produto_preco'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorito',
            unique_together={('usuario', 'produto')},
        ),
    ]