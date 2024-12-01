from datetime import datetime
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('', views.home, name='home'),  # Главная страница
    path('contact/', views.contact, name='contact'),  # Страница контактов
    path('about/', views.about, name='about'),  # Страница о нас
    path('links/', views.links, name='links'),  # Полезные ресурсы
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),  # Вход
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Выход
    path('benefits/', views.benefits_content, name='benefits_content'),  # Преимущества
    path('pool/', views.pool, name='pool'),  # Обратная связь
    path('thank_you/', views.thank_you, name='thank_you'),  # Страница благодарности
    path('registration/', views.registration, name='registration'),  # Регистрация
    path('blog/', views.blog, name='blog'),  # Блог
    path('blog/<int:parametr>/', views.blogpost, name='blogpost'),  # Страница конкретного поста
    path('newpost/', views.newpost, name='newpost'),  # Добавление нового поста
    path('videopost/', views.videopost, name='videopost'),  # Видео пост
    path('cart/', views.cart, name='cart'),  # Корзина
    path('products/', views.products, name='products'),  # Страница продуктов
    path('bike/<int:bike_id>/', views.bike_detail, name='bike_detail'),  # Страница конкретного велосипеда
    path('bike/<int:bike_id>/add_review/', views.add_review, name='add_review'),  # Добавление отзыва
    path('bike/<int:bike_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),  # Добавление в корзину
    path('cart/remove/<int:item_id>/', views.remove_item, name='remove_item'),  # Удаление товара из корзины
    path('cart/remove_all/<int:item_id>/', views.remove_all_items, name='remove_all_items'),  # Удаление всех товаров из строки
    
]

# Обработка статических и медиа файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
