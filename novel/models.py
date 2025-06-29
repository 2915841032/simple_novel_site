from datetime import datetime
from django.db import models


class Category(models.Model):
    """小说分类"""
    name = models.CharField(max_length=20, verbose_name="分类名称")
    description = models.TextField(blank=True, verbose_name="分类描述")
    
    class Meta:
        verbose_name = "小说分类"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name


class Novel(models.Model):
    """小说信息"""
    title = models.CharField(max_length=100, verbose_name="小说标题")
    author = models.CharField(max_length=50, verbose_name="作者")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    cover = models.ImageField(upload_to="novel_covers/", blank=True, verbose_name="封面")
    description = models.TextField(blank=True, verbose_name="简介")
    word_count = models.IntegerField(default=0, verbose_name="字数")
    view_count = models.IntegerField(default=0, verbose_name="阅读量")
    is_completed = models.BooleanField(default=False, verbose_name="是否完结")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "小说"
        verbose_name_plural = verbose_name
        ordering = ['-updated_time']
        
    def __str__(self):
        return self.title


class Chapter(models.Model):
    """小说章节"""
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name="所属小说")
    title = models.CharField(max_length=200, verbose_name="章节标题")
    content = models.TextField(verbose_name="章节内容")
    chapter_number = models.IntegerField(verbose_name="章节序号")
    word_count = models.IntegerField(default=0, verbose_name="字数")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name
        ordering = ['chapter_number']
        unique_together = ['novel', 'chapter_number']
        
    def __str__(self):
        return f"{self.novel.title} - {self.title}"
    
    def save(self, *args, **kwargs):
        # 自动计算字数
        self.word_count = len(self.content)
        super().save(*args, **kwargs) 