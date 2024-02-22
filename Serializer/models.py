from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=250)
    body=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title