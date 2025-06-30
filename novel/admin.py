from django.contrib import admin
from .models import Category, Novel, Chapter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1
    fields = ['title', 'chapter_number', 'word_count']


@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'word_count', 'view_count', 'is_completed', 'updated_time']
    list_filter = ['category', 'is_completed', 'created_time']
    search_fields = ['title', 'author', 'description']
    inlines = [ChapterInline]
    readonly_fields = ['word_count', 'view_count']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'novel', 'chapter_number', 'word_count', 'created_time']
    list_filter = ['novel', 'created_time']
    search_fields = ['title', 'content']
    ordering = ['novel', 'chapter_number'] 