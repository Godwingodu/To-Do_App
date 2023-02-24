from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):

     status_choices=[
          ('COMPLETED','COMPLETED'),
          ('PENDING','PENDING')
     ]
     priority_choices=[
          ('1','1'),
          ('2','2'),
          ('3','3'),
          ('4','4'),
          ('5','5'),
          ('6','6'),
          ('7','7'),
          ('8','8'),
          ('9','9'),
          ('10','10'),
     ]
     title=models.CharField(max_length=50)
     description=models.CharField(max_length=50,blank=True)
     status=models.CharField(max_length=10,choices=status_choices)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateTimeField(auto_now_add=True)
     priority=models.CharField(max_length=2,choices=priority_choices)