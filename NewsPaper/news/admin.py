from django.contrib import admin
from .models import Author, Post, PostCategory, Comment, Category
from modeltranslation.admin import TranslationAdmin



# admin.site.register(Author)

admin.site.register(Author)
admin.site.register(Category)
<<<<<<< Updated upstream
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
=======
admin.site.register(Comment)
admin.site.register(Post, ProductAdmin)


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


>>>>>>> Stashed changes
