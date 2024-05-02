# Gin Index Tests

A repo for testing index creation of GIN  indexes using Django.
It has one model `Article` with two fields `header`, `content`, and tries
to create a gin index on `UPPER("header")`.

## Installation

1. `pip install -r requirements.txt`
2. `CREATE DATABASE gin_index_test;`
3. Optional: you might have to change USER/PASSWORD in the settings.py file if
   you are not using the default postgres/postgres combo.

## Reproducing the error:

Run:

`python manage.py migrate`

You should see:


```
django.db.utils.ProgrammingError: syntax error at or near "gin_trgm_ops"
LINE 1: ...ON "articles_article" USING gin ((UPPER("header") gin_trgm_o...
```

## Cause:

Django is trying to run the following SQL:

```sh
python manage.py sqlmigrate articles 0003
```
```sql
CREATE INDEX "article_gin_upper_header" ON "articles_article" USING gin ((UPPER("header") gin_trgm_ops));
```

When the correct should be:

```sql
CREATE INDEX "article_gin_upper_header" ON "articles_article" USING gin ((UPPER("header")) gin_trgm_ops);
```

(subtle change in parenthesis).
