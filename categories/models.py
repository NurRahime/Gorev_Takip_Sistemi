from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, default="primary")

    def _str_(self):
        return self.name