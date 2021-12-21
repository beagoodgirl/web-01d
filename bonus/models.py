from django.db import models
from django.urls import reverse

# Create your models here.


class Prize(models.Model):
    pid = models.CharField(max_length=25)
    cname = models.CharField(max_length=20)
    amount = models.IntegerField()
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="images/", null=True, blank=True)

    def get_url(self):
        return reverse('prize-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['-amount']
    
    def __str__(self):
        return self.cname


class Winner(models.Model):
    prize_id = models.ForeignKey(
        "Prize", on_delete=models.CASCADE)
    week = models.CharField(max_length=1, default='1')
    last_ssn = models.CharField(max_length=3)
    
    class Meta:
        ordering = ['week', 'prize_id']
        
    def __str__(self):
        return self.prize_id.cname + ", Week" + self.week + ", "+ self.last_ssn

