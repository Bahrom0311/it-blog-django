from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    image = models.ImageField(upload_to='news_images/', verbose_name="Rasm")
    content = models.TextField(verbose_name="Maqola matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at'] # Eng yangisi tepadaturadi