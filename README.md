# 简单小说网站

一个精简的Django小说网站，专注于小说阅读和搜索功能。

## 功能特性

- 📚 小说浏览和阅读
- 🔍 全文搜索功能
- 📱 响应式设计
- 📂 分类管理
- 📖 章节阅读
- 📊 阅读统计

## 技术栈

- **后端**: Django 4.2+
- **前端**: Bootstrap 5 + Font Awesome
- **数据库**: SQLite (可配置为MySQL/PostgreSQL)
- **图片处理**: Pillow

## 安装和运行

### 1. 克隆项目
```bash
git clone <repository-url>
cd simple_novel_site
```

### 2. 创建虚拟环境
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 创建超级用户
```bash
python manage.py createsuperuser
```

### 6. 运行开发服务器
```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000 查看网站

## 项目结构

```
simple_novel_site/
├── manage.py
├── requirements.txt
├── README.md
├── simple_novel/          # Django项目配置
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── novel/                 # 小说应用
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/             # 模板文件
│   ├── base.html
│   └── novel/
│       ├── index.html
│       ├── novel_detail.html
│       ├── chapter_detail.html
│       ├── search.html
│       └── category.html
├── media/                 # 媒体文件
└── static/                # 静态文件
```

## 数据模型

### Category (分类)
- name: 分类名称
- description: 分类描述

### Novel (小说)
- title: 小说标题
- author: 作者
- category: 分类
- cover: 封面图片
- description: 简介
- word_count: 字数
- view_count: 阅读量
- is_completed: 是否完结
- created_time: 创建时间
- updated_time: 更新时间

### Chapter (章节)
- novel: 所属小说
- title: 章节标题
- content: 章节内容
- chapter_number: 章节序号
- word_count: 字数
- created_time: 创建时间

## 主要功能

### 1. 首页
- 轮播图展示推荐小说
- 最新小说列表
- 热门小说推荐
- 分页浏览

### 2. 小说详情页
- 小说基本信息
- 章节列表
- 阅读量统计

### 3. 章节阅读页
- 章节内容展示
- 上一章/下一章导航
- 阅读体验优化

### 4. 搜索功能
- 支持标题、作者、简介搜索
- 搜索结果分页
- 搜索建议

### 5. 分类浏览
- 按分类筛选小说
- 分类标签导航

## 管理后台

访问 http://127.0.0.1:8000/admin 进入管理后台

可以管理：
- 小说分类
- 小说信息
- 章节内容

## 部署说明

### 生产环境配置

1. 修改 `settings.py` 中的配置：
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
```

2. 配置数据库（推荐使用MySQL或PostgreSQL）

3. 收集静态文件：
```bash
python manage.py collectstatic
```

4. 使用Gunicorn或uWSGI部署

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v1.0.0
- 初始版本发布
- 基础小说阅读功能
- 搜索和分类功能
- 响应式设计 