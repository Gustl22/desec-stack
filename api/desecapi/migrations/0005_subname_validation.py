# Generated by Django 3.1 on 2020-09-08 14:01

import desecapi.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desecapi', '0004_immortal_domains'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rrset',
            name='subname',
            field=models.CharField(blank=True, max_length=178, validators=[desecapi.models.validate_lower, django.core.validators.RegexValidator(code='invalid_subname', message="Subname can only use (lowercase) a-z, 0-9, ., -, and _, may start with a '*.', or just be '*'.", regex='^([*]|(([*][.])?([a-z0-9_-]+[.])*[a-z0-9_-]+))$')]),
        ),
    ]