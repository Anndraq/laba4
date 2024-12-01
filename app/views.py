from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, BlogForm, CommentForm, BootstrapAuthenticationForm, ReviewForm
from .models import Blog, Comment, Feedback, Bike, CartItem, Review

def home(request):
    return render(request, 'app/index.html', {'title': 'Главная', 'year': datetime.now().year})

def contact(request):
    return render(request, 'app/contact.html', {'title': 'Контакты', 'year': datetime.now().year})

def about(request):
    return render(request, 'app/about.html', {'title': 'О нас', 'year': datetime.now().year})

def links(request):
    return render(request, 'app/links.html', {'title': 'Полезные ресурсы', 'year': datetime.now().year})

def benefits_content(request):
    return render(request, 'app/benefits_content.html', {'title': 'Преимущества велотренажеров', 'year': datetime.now().year})

def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            request.session['submitted_data'] = form.cleaned_data
            return redirect('thank_you')
    else:
        form = FeedbackForm()

    return render(request, 'app/pool.html', {'title': 'Обратная связь', 'form': form, 'year': datetime.now().year})

def thank_you(request):
    submitted_data = request.session.get('submitted_data', {})
    return render(request, 'app/thank_you.html', {'title': 'Спасибо за отзыв', 'submitted_data': submitted_data, 'year': datetime.now().year})

def registration(request):
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            login(request, reg_f)
            return redirect('home')
    else:
        regform = UserCreationForm()

    return render(request, 'app/registration.html', {'regform': regform, 'year': datetime.now().year})

def blog(request):
    posts = Blog.objects.all()
    return render(request, 'app/blog.html', {'title': 'Блог', 'posts': posts, 'year': datetime.now().year})

def blogpost(request, parametr):
    post_1 = get_object_or_404(Blog, id=parametr)
    comments = Comment.objects.filter(post=post_1).order_by('-date')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = timezone.now()
            comment_f.post = post_1
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()

    return render(request, 'app/blogpost.html', {'post': post_1, 'comments': comments, 'form': form, 'year': datetime.now().year})

def newpost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()

    return render(request, 'app/newpost.html', {'form': form, 'year': datetime.now().year})

def videopost(request):
    return render(request, 'app/videopost.html', {'title': 'Видео', 'year': datetime.now().year})

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'app/cart.html', {'title': 'Корзина', 'cart_items': cart_items, 'year': datetime.now().year})

@login_required
def products(request):
    bikes = Bike.objects.all()

    # Получаем количество товаров в корзине для текущего пользователя
    bike_quantities = {item.bike.id: item.quantity for item in CartItem.objects.filter(user=request.user)}

    return render(request, 'app/products.html', {
        'bikes': bikes,
        'bike_quantities': bike_quantities,  # Передаем bike_quantities как словарь
        'year': datetime.now().year  # Добавляем текущий год в контекст
    })

@login_required
def bike_detail(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    reviews = Review.objects.filter(bike=bike).order_by('-created_at')  # Получаем отзывы для данного велосипеда

    # Получаем количество товаров в корзине для текущего пользователя
    bike_quantities = {item.bike.id: item.quantity for item in CartItem.objects.filter(user=request.user)}

    return render(request, 'app/bike_detail.html', {
        'bike': bike,
        'reviews': reviews,
        'bike_quantities': bike_quantities,
        'title': bike.name,
        'year': datetime.now().year  # Добавляем текущий год в контекст
    })

@login_required
def add_review(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.bike = bike
            review.user = request.user
            review.save()
            return redirect('bike_detail', bike_id=bike_id)
    else:
        form = ReviewForm()

    return render(request, 'app/add_review.html', {
        'form': form,
        'bike': bike,
        'year': datetime.now().year  # Добавляем текущий год в контекст
    })

@login_required
def add_to_cart(request, bike_id):
    if request.method == 'POST':
        bike = get_object_or_404(Bike, id=bike_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, bike=bike)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Получаем количество товаров в корзине для текущего пользователя
        bike_quantities = {item.bike.id: item.quantity for item in CartItem.objects.filter(user=request.user)}

        return JsonResponse({'success': True, 'quantity': cart_item.quantity, 'cart': bike_quantities})

    return JsonResponse({'success': False}, status=400)

@login_required
def remove_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart')

@login_required
def remove_all_items(request, item_id):
    if request.method == 'POST':
        CartItem.objects.filter(id=item_id).delete()
        return redirect('cart')
