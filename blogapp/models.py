from django.db import models

class Maqola(models.Model):
    sarlovha = models.CharField(max_length=200)
    sana = models.DateField(auto_now_add=True)
    matn = models.TextField()
    rasm = models.FileField()
    def __str__(self):
        return self.sarlovha

class Interviyu(models.Model):
    link = models.URLField()
    sana = models.DateField(auto_now_add=True)
    sarlovha = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.sarlovha}, ({self.sana})"