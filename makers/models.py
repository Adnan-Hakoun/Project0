from django.db import models


class Maker(models.Model):
    title=          models.CharField(max_length=120)
    nationality=    models.CharField(max_length=120)
    def __str__ (self):
        return self.title
