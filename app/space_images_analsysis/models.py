from django.db import models

class SpaceImagesAnalysis(models.Model):
    weights = models.FloatField()
    bias = models.FloatField()
    predicted_num_stars = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()