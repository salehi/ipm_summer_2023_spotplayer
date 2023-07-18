from django.db import models


class SpotPlayer(models.Model):
    national_code = models.TextField()
    registry_code = models.TextField()
    key = models.TextField()
