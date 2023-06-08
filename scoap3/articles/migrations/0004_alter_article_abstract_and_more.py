# Generated by Django 4.2.2 on 2023-06-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("misc", "0005_alter_affiliation_organization_and_more"),
        (
            "articles",
            "0003_alter_article_abstract_alter_article_acceptance_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="abstract",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="related_licenses",
            field=models.ManyToManyField(
                related_name="related_licenses", to="misc.license"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="related_materials",
            field=models.ManyToManyField(
                blank=True, related_name="related_articles", to="misc.relatedmaterial"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="subtitle",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.TextField(),
        ),
    ]
