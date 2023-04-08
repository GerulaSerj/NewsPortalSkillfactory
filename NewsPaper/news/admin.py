from django.contrib import admin
from .models import Author, Post, PostCategory, Comment, Category

# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('author', 'rating', 'title', 'dateCreation')
    list_filter = ('author', 'rating', 'postCategory', 'dateCreation')
    search_fields = ('author', 'rating', 'title', 'postCategory')

# Регистрация моделей
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, ProductAdmin)