from django.db import models

# Create your models here.
class URLModel(models.Model):
    longURL = models.URLField(max_length=256)
    shortURL = models.CharField(max_length= 7, null=False, blank=False)
    createDate = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.longURL} {self.shortURL} {self.createDate}"