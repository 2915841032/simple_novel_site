from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Novel, Chapter, Category


class IndexView(ListView):
    """首页视图"""
    model = Novel
    template_name = 'novel/index.html'
    context_object_name = 'novels'
    paginate_by = 12
    
    def get_queryset(self):
        return Novel.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['latest_novels'] = Novel.objects.order_by('-created_time')[:6]
        context['popular_novels'] = Novel.objects.order_by('-view_count')[:6]
        return context


class NovelDetailView(DetailView):
    """小说详情页"""
    model = Novel
    template_name = 'novel/novel_detail.html'
    context_object_name = 'novel'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        novel = self.get_object()
        # 增加阅读量
        novel.view_count += 1
        novel.save()
        
        # 获取章节列表
        chapters = novel.chapter_set.all()
        context['chapters'] = chapters
        context['total_chapters'] = chapters.count()
        context['latest_chapter'] = chapters.last()
        return context


class ChapterDetailView(DetailView):
    """章节阅读页"""
    model = Chapter
    template_name = 'novel/chapter_detail.html'
    context_object_name = 'chapter'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapter = self.get_object()
        novel = chapter.novel
        
        # 获取上一章和下一章
        prev_chapter = Chapter.objects.filter(
            novel=novel, 
            chapter_number__lt=chapter.chapter_number
        ).order_by('-chapter_number').first()
        
        next_chapter = Chapter.objects.filter(
            novel=novel, 
            chapter_number__gt=chapter.chapter_number
        ).order_by('chapter_number').first()
        
        context['novel'] = novel
        context['prev_chapter'] = prev_chapter
        context['next_chapter'] = next_chapter
        return context


class CategoryView(ListView):
    """分类页面"""
    model = Novel
    template_name = 'novel/category.html'
    context_object_name = 'novels'
    paginate_by = 12
    
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Novel.objects.filter(category_id=category_id)
        return Novel.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.kwargs.get('category_id')
        return context


def search_view(request):
    """搜索功能"""
    query = request.GET.get('q', '')
    novels = []
    
    if query:
        novels = Novel.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    
    # 分页
    paginator = Paginator(novels, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'novels': page_obj,
        'query': query,
        'total_results': len(novels),
    }
    
    return render(request, 'novel/search.html', context) 