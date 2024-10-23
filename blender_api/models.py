from django.db import models


# Create your models here.
class SceneData(models.Model):
    username = models.CharField(max_length=100)
    save_time = models.DateTimeField()
    filepath = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} - {self.save_time}"
