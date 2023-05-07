from django.urls import path
<<<<<<< Updated upstream
# Импортируем созданные нами представления
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticlesCreate, ArticlesUpdate, ArticlesDelete

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
=======

from .views import (PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticlesCreate,
   ArticlesUpdate, ArticlesDelete, subscriptions, IndexView
)
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60)(PostList.as_view()), name='post_list'),
   path('<int:pk>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('search/', cache_page(300)(PostSearch.as_view()), name='post_search'),
   path('create/', cache_page(300)(PostCreate.as_view()), name='post_create'),
   path('<int:pk>/update/', cache_page(300)(PostUpdate.as_view()), name='post_update'),
   path('<int:pk>/delete/', cache_page(300)(PostDelete.as_view()), name='post_delete'),
   path('articles/create/', cache_page(300)(ArticlesCreate.as_view()), name='articles_create'),
   path('articles/<int:pk>/update/', cache_page(300)(ArticlesUpdate.as_view()), name='articles_update'),
   path('articles/<int:pk>/delete/', cache_page(300)(ArticlesDelete.as_view()), name='articles_delete'),
   path('<int:pk>/', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('', IndexView.as_view()),
>>>>>>> Stashed changes
]