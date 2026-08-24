# Initial migration

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("numero_patrimonio", models.IntegerField(default=0)),
                ("tipo", models.CharField(max_length=150)),
                ("em_uso", models.BooleanField(default=False)),
            ],
        ),
    ]
