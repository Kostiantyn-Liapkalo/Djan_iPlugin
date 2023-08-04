# Generated by Django 4.2 on 2023-05-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_alter_author_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.TextField(default='data:image/png;base64,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'),
        ),
    ]
