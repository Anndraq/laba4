from django.contrib import admin
from .models import Bike, Blog, Comment, Feedback, CartItem, Review
# Регистрация модели в административном разделе
admin.site.register(Bike)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Feedback)
admin.site.register(Review)
admin.site.register(CartItem)