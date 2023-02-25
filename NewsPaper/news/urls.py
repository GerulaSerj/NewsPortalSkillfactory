from django.urls import path
# Импортируем созданные нами представления
<<<<<<< Updated upstream
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticlesCreate, ArticlesUpdate, ArticlesDelete
=======
from .views import (PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticlesCreate,
   ArticlesUpdate, ArticlesDelete, subscriptions, IndexView
)
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('', IndexView.as_view()),
>>>>>>> Stashed changes
]