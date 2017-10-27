from django.db import models

# Create your models here.


class Languages(models.Model):
    display_name = models.CharField(max_length=255)
    language_code = models.CharField(max_length=10)
    version = models.CharField(max_length=20, default=None)

    class Meta:
        db_table = 'languages'
