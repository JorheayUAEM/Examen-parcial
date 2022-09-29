from django.db import models

# Create your models here.

class genNum(models.Model):
    val1 = models.IntegerField(blank=True, null=True)
    val2 = models.CharField(max_length=1024)
    val3 = models.IntegerField(blank=True, null=True)
    val4 = models.IntegerField(blank=True, null=True)

    def str(self):
        return str(self.val1), str(self.val2), str(self.val3), str(self.val4)