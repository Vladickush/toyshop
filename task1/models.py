from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True) # имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс покупателя
    age = models.PositiveIntegerField()  # возраст покупателя

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100, unique=True) # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер файлов игры
    description = models.TextField(blank=True)  # Описание игры
    age_limited = models.BooleanField(default=False)    # ограничение возраста 18+
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Связь "многие ко многим"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
