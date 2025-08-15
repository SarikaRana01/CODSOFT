from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField(null=False,blank=False)
    descp=models.CharField(1024,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)
    # priority=models.TextField(choices=[("high","high"),("medium","medium"),("low","low")],null=False)
    priority = models.CharField(max_length=10, choices=[("high","high"),("medium","medium"),("low","low")],null=True,default="low",blank=True)
    is_completed=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} {self.title}"