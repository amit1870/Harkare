from django.db import models

class Kathakar(models.Model):
    nam = models.CharField(max_length=255)
    prasidha_nam = models.CharField(max_length=255, blank=True)
    gaon = models.CharField(max_length=255)
    janam_tithi = models.DateTimeField(auto_now=False, auto_now_add=False)
    vriti = models.CharField(max_length=255, blank=True)

class Katha(models.Model):
    kathakar = models.ForeignKey(Kathakar, on_delete=models.CASCADE)
    nam = models.CharField(max_length=255)


