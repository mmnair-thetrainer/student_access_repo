from django.db import models


class Facebook(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "facebook"
