from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_id", models.CharField(max_length=255)),
                ("order_date", models.DateTimeField()),
                ("total_amount", models.CharField(max_length=255)),
                ("checked_out", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Order_Details",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.CharField(max_length=255)),
                ("product_id", models.CharField(max_length=255)),
                ("quantity", models.CharField(max_length=255)),
                ("price", models.CharField(max_length=255)),
            ],
        ),
    ]
