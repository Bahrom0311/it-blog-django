from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Bosh sahifa (Hamma yangiliklar)
def home_view(request):
    posts = Post.objects.all()
    categories = Category.objects.all()  # Sidebar uchun kategoriyalar
    
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'home.html', context)

# Kategoriya bo'yicha filtrlash
def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category) # Faqat shu kategoriyadagi postlar
    categories = Category.objects.all()  # Sidebar yo'qolib qolmasligi uchun yana olamiz

    context = {
        'posts': posts,
        'categories': categories,
        'current_category': category # Qaysi kategoriya tanlanganini bilish uchun
    }
    return render(request, 'home.html', context)

# Batafsil sahifa (o'zgarishsiz qoladi)
def detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})