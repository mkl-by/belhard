from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='название',
        help_text='вводи пальцами'
        )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books'
    )
    data_publish = models.DateField(auto_now_add=True, db_index=True)
    likes = models.ManyToManyField(User, related_name='liked_books')






    def __str__(self):
        return self.title



