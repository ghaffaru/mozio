from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_provider_email_alter_provider_phonenumber"),
    ]

    operations = [
        CreateExtension("postgis"),
    ]