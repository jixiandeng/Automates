# Generated by Django 4.1 on 2024-12-06 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automates_app', '0006_draft_audience_textbox_draft_style_textbox_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draft',
            name='audience_textbox',
        ),
        migrations.RemoveField(
            model_name='draft',
            name='style_textbox',
        ),
        migrations.RemoveField(
            model_name='draft',
            name='tone_textbox',
        ),
    ]
