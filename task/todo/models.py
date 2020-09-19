from django.db import models

# Create your models here.
class ToDo(models.Model):
    todo_name = models.CharField(max_length=100)

    def __str__(self):
        return self.todo_name