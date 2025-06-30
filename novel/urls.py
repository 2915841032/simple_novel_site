from django.urls import path
from . import views

app_name = 'novel'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('novel/<int:pk>/', views.NovelDetailView.as_view(), name='novel_detail'),
    path('chapter/<int:pk>/', views.ChapterDetailView.as_view(), name='chapter_detail'),
    path('category/<int:category_id>/', views.CategoryView.as_view(), name='category'),
    path('search/', views.search_view, name='search'),
] 