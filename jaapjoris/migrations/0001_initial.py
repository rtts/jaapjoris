import cms.fields
import cms.mixins
import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("title", cms.fields.CharField()),
                ("slug", cms.fields.SlugField(unique=True)),
                ("number", cms.fields.PositiveIntegerField()),
                ("menu", cms.fields.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "page",
                "verbose_name_plural": "pages",
                "ordering": ["number"],
                "abstract": False,
            },
            bases=(cms.mixins.Numbered, models.Model),
        ),
        migrations.CreateModel(
            name="Section",
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
                ("title", cms.fields.CharField()),
                ("type", cms.fields.CharField()),
                ("number", cms.fields.PositiveIntegerField()),
                ("content", cms.fields.TextField()),
                ("image", cms.fields.ImageField()),
                (
                    "video",
                    embed_video.fields.EmbedVideoField(
                        blank=True,
                        help_text="Paste a YouTube, Vimeo, or SoundCloud link",
                        verbose_name="video",
                    ),
                ),
                ("href", cms.fields.CharField()),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sections",
                        to="jaapjoris.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "section",
                "verbose_name_plural": "sections",
                "ordering": ["number"],
                "abstract": False,
            },
            bases=(cms.mixins.Numbered, models.Model),
        ),
    ]
