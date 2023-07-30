# Generated by Django 4.2.3 on 2023-07-30 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("produit", "0002_tag_produit_tag"),
        ("commande", "0005_remove_commande_produit_commande_produits"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="commande",
            name="produits",
        ),
        migrations.AddField(
            model_name="commande",
            name="produits",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="produit.produit",
            ),
        ),
    ]