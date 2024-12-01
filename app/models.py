from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    short_content = models.TextField(verbose_name="Краткое содержание")
    full_content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['-posted']

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    class Meta:
        ordering = ['-date']

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    rating = models.IntegerField(verbose_name="Оценка сайта", default=0)
    comments = models.TextField(verbose_name="Комментарии")
    subscribe = models.BooleanField(default=False, verbose_name="Подписаться на новости")
    suggestions = models.TextField(blank=True, null=True, verbose_name="Предложения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

class Bike(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bikes/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    bike = models.ForeignKey('Bike', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    оценка = models.IntegerField(null=False, blank=False)
    комментарий = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.bike.name}'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)  # Изменено на связь с моделью Bike
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.bike.name} (x{self.quantity})"
