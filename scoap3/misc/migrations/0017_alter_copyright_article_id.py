# Generated by Django 4.2.5 on 2023-11-01 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0011_alter_articleidentifier_article_id"),
        ("misc", "0016_alter_articlearxivcategory_article_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="copyright",
            name="article_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="copyright",
                to="articles.article",
            ),
        ),
    ]