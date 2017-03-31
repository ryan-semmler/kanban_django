from django.db import models


STATUS_CHOICE = [(1,"not started"), (2, "in progress"), (3, "completed")]
PRIORITY_CHOICE = [(1, "low priority"), (2, "medium-rare priority"), (3, "medium priority"), (4, "medium-well priority"), (5, "top priority")]

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="(1, not started)")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICE, default="(1, low priority)")
    # user = models.ForeignKey(User)
