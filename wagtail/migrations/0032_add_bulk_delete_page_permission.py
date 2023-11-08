# Generated by Django 1.10.1 on 2016-09-27 14:11
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0031_add_page_view_restriction_types"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grouppagepermission",
            name="permission_type",
            field=models.CharField(
                choices=[
                    ("add", "Add/edit pages you own"),
                    ("edit", "Edit any page"),
                    ("publish", "Publish any page"),
                    ("bulk_delete", "Delete pages with children"),
                    ("lock", "Lock/unlock any page"),
                ],
                max_length=20,
                verbose_name="permission type",
            ),
        ),
    ]
