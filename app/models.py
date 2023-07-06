from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Record(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    dept = models.CharField(max_length=50,default="")
    year = models.IntegerField(default=1)
    sem = models.IntegerField(default=1)
    day = models.DateField(auto_now=False, auto_now_add=False)
    hour1 = models.BooleanField(default=False)
    hour2 = models.BooleanField(default=False)
    hour3 = models.BooleanField(default=False)
    hour4 = models.BooleanField(default=False)
    hour5 = models.BooleanField(default=False)
    hour6 = models.BooleanField(default=False)
    hour7 = models.BooleanField(default=False)
    hour8 = models.BooleanField(default=False)

    def __str__(self):
        s = str(self.user.username) + '-'+ str(self.day.month) +'/' + str(self.day.day)
        return s
    

