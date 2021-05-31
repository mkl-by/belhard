from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    likes = models.ManyToManyField(User, related_name='liked_books', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    deta = models.DateTimeField(auto_now_add=True)
   # on_delete = models.SET_DEFAULT, показать по дефолту юзера
    #default = 4, дефолтное значение
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=4,
        related_name='comment')
    #like = models.ManyToManyField(User, related_name='like_comment', blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')

    avg_rate = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=True,
        blank=True
    )
    # rate = models.ManyToManyField(
    #     User,
    #     related_name='rated_book',
    #     blank=True,
    #     through="UserRateBook"
    # )

class UserRateBook(models.Model):
    class Meta:
        unique_together = ('user', 'book')

    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )