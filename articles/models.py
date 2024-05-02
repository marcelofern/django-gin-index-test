from django.db import models
from django.contrib.postgres import indexes as pg_indexes

class Article(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        indexes = (
            pg_indexes.GinIndex(
                pg_indexes.OpClass(
                    models.functions.Upper("header"), name="gin_trgm_ops"
                ),
                name="article_gin_upper_header",
            ),
        )
