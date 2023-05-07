from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import PostListAPIView, PostDetailAPIView, PostCategoryListAPIView, PostCategoryDetailAPIView
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'posts', PostListAPIView, basename='post')
router.register(r'post/(?P<pk>\d+)', PostDetailAPIView, basename='post-detail')
router.register(r'post-categories', PostCategoryListAPIView, basename='post-category')
router.register(r'post-category/(?P<pk_category>\d+)', PostCategoryDetailAPIView, basename='post-category-detail')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('news.urls')),
   path('search/', include('news.urls')),
   path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией
   path('', include('news.urls')),
   path('news/', PostListAPIView.as_view({'get': 'list'}), name='post_list'),
   path('news/<int:pk>/', PostDetailAPIView.as_view({'get': 'retrieve'}), name='post_detail'),
   path('articles/', PostCategoryListAPIView.as_view({'get': 'list'}), name='postcategory_list'),
   path('articles/<int:pk>/', PostCategoryDetailAPIView.as_view({'get': 'retrieve'}), name='postcategory_detail'),
   path('', include(router.urls)),
   path('swagger-ui/', TemplateView.as_view(
       template_name='swagger-ui.html',
       extra_context={'schema_url':'openapi-schema'}
   ), name='swagger-ui'),
]