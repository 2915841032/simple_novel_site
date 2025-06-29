#!/usr/bin/env python
"""
创建示例数据的脚本
运行方式: python create_sample_data.py
"""

import os
import sys
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_novel.settings')
django.setup()

from novel.models import Category, Novel, Chapter

def create_sample_data():
    """创建示例数据"""
    
    # 创建分类
    categories = [
        {'name': '玄幻', 'description': '玄幻小说，包含魔法、修炼等元素'},
        {'name': '都市', 'description': '都市生活类小说'},
        {'name': '历史', 'description': '历史背景的小说'},
        {'name': '科幻', 'description': '科幻类小说'},
        {'name': '武侠', 'description': '武侠小说'},
    ]
    
    created_categories = []
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        created_categories.append(category)
        if created:
            print(f"创建分类: {category.name}")
    
    # 创建小说
    novels_data = [
        {
            'title': '修真世界',
            'author': '方想',
            'category': '玄幻',
            'description': '一个普通的少年，因为一次意外，踏上了修真之路。在这个充满危险和机遇的世界里，他必须不断变强，才能保护自己和身边的人。',
            'is_completed': False
        },
        {
            'title': '都市之最强狂兵',
            'author': '烈焰滔滔',
            'category': '都市',
            'description': '特种兵王回归都市，开启了一段传奇人生。在这个繁华的都市中，他将用自己的实力和智慧，书写属于自己的传奇。',
            'is_completed': False
        },
        {
            'title': '大明王朝',
            'author': '历史爱好者',
            'category': '历史',
            'description': '穿越到明朝，成为一位普通的读书人。在这个风云变幻的时代，他将如何在这个历史的大舞台上展现自己的才华？',
            'is_completed': True
        },
        {
            'title': '星际征途',
            'author': '科幻作家',
            'category': '科幻',
            'description': '在遥远的未来，人类已经踏上了星际探索的道路。在这个浩瀚的宇宙中，人类将面临怎样的挑战和机遇？',
            'is_completed': False
        },
        {
            'title': '剑侠风云录',
            'author': '武侠大师',
            'category': '武侠',
            'description': '一个普通的少年，因为一次机缘巧合，得到了一本绝世武功秘籍。从此，他踏上了成为一代大侠的道路。',
            'is_completed': True
        }
    ]
    
    created_novels = []
    for novel_data in novels_data:
        category = next(cat for cat in created_categories if cat.name == novel_data['category'])
        novel, created = Novel.objects.get_or_create(
            title=novel_data['title'],
            defaults={
                'author': novel_data['author'],
                'category': category,
                'description': novel_data['description'],
                'is_completed': novel_data['is_completed'],
                'word_count': 0
            }
        )
        created_novels.append(novel)
        if created:
            print(f"创建小说: {novel.title}")
    
    # 为每本小说创建章节
    for novel in created_novels:
        chapter_count = 5 if novel.is_completed else 3
        
        for i in range(1, chapter_count + 1):
            chapter_title = f"第{i}章"
            if novel.title == '修真世界':
                chapter_content = f"""
                第{i}章 修真之路的开始

                清晨的阳光透过窗户洒在少年的脸上，他缓缓睁开眼睛，感受着体内那一丝若有若无的灵气。

                这是修真的开始，也是他命运的转折点。

                在这个充满危险和机遇的世界里，他必须不断变强，才能保护自己和身边的人。

                修真之路，漫长而艰辛，但他已经做好了准备。

                "我一定要成为最强的修真者！"少年握紧拳头，眼中闪烁着坚定的光芒。

                这一天，注定是不平凡的一天。
                """
            elif novel.title == '都市之最强狂兵':
                chapter_content = f"""
                第{i}章 回归都市

                飞机缓缓降落在机场，一个身材魁梧的男子从机舱中走出。

                他就是曾经的兵王，如今回归都市，准备开始新的人生。

                都市的繁华让他有些不适，但很快他就适应了这里的生活节奏。

                在这个充满挑战的都市中，他将用自己的实力和智慧，书写属于自己的传奇。

                "都市，我来了！"男子望着远方的高楼大厦，眼中闪过一丝兴奋。
                """
            elif novel.title == '大明王朝':
                chapter_content = f"""
                第{i}章 穿越明朝

                一阵眩晕过后，他发现自己来到了一个陌生的地方。

                这里是大明王朝，一个他只在历史书上读到过的朝代。

                作为一个现代人，他拥有着超越这个时代的知识和见识。

                在这个风云变幻的时代，他将如何在这个历史的大舞台上展现自己的才华？

                "既然来了，就要好好干一番事业！"他暗暗下定决心。
                """
            elif novel.title == '星际征途':
                chapter_content = f"""
                第{i}章 星际探索

                在遥远的未来，人类已经踏上了星际探索的道路。

                宇宙飞船在浩瀚的星空中航行，寻找着新的家园和资源。

                在这个充满未知的宇宙中，人类将面临怎样的挑战和机遇？

                每一次的探索都是一次冒险，每一次的发现都是一次惊喜。

                "宇宙，我们来了！"船长望着前方的星云，心中充满了期待。
                """
            else:  # 剑侠风云录
                chapter_content = f"""
                第{i}章 武林秘籍

                一个普通的少年，因为一次机缘巧合，得到了一本绝世武功秘籍。

                从此，他踏上了成为一代大侠的道路。

                武林中的恩怨情仇，江湖中的刀光剑影，都将成为他成长路上的考验。

                在这个充满危险的武林中，他必须不断变强，才能保护自己和身边的人。

                "我一定要成为一代大侠！"少年握紧手中的秘籍，眼中闪烁着坚定的光芒。
                """
            
            chapter, created = Chapter.objects.get_or_create(
                novel=novel,
                chapter_number=i,
                defaults={
                    'title': chapter_title,
                    'content': chapter_content.strip(),
                    'word_count': len(chapter_content)
                }
            )
            
            if created:
                print(f"  创建章节: {novel.title} - {chapter_title}")
    
    # 更新小说的字数统计
    for novel in created_novels:
        total_words = sum(chapter.word_count for chapter in novel.chapter_set.all())
        novel.word_count = total_words
        novel.save()
        print(f"更新小说字数: {novel.title} - {total_words} 字")
    
    print("\n示例数据创建完成！")
    print(f"创建了 {len(created_categories)} 个分类")
    print(f"创建了 {len(created_novels)} 本小说")
    print("现在可以运行 'python manage.py runserver' 启动网站")

if __name__ == '__main__':
    create_sample_data() 