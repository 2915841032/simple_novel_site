#!/usr/bin/env python
"""
快速启动脚本
自动完成数据库迁移、创建超级用户和启动服务器
"""

import os
import sys
import subprocess
import django

def run_command(command, description):
    """运行命令并显示结果"""
    print(f"\n{'='*50}")
    print(f"正在执行: {description}")
    print(f"命令: {command}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ 执行成功!")
        if result.stdout:
            print("输出:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ 执行失败!")
        print("错误:", e.stderr)
        return False

def main():
    """主函数"""
    print("🚀 简单小说网站快速启动")
    print("="*50)
    
    # 检查Python版本
    if sys.version_info < (3, 8):
        print("❌ 需要Python 3.8或更高版本")
        return
    
    # 检查是否在正确的目录
    if not os.path.exists('manage.py'):
        print("❌ 请在项目根目录运行此脚本")
        return
    
    # 1. 安装依赖
    print("\n📦 步骤1: 安装依赖")
    if not run_command("pip install -r requirements.txt", "安装项目依赖"):
        print("❌ 依赖安装失败，请检查网络连接或手动安装")
        return
    
    # 2. 数据库迁移
    print("\n🗄️ 步骤2: 数据库迁移")
    if not run_command("python manage.py makemigrations", "创建数据库迁移文件"):
        print("❌ 创建迁移文件失败")
        return
    
    if not run_command("python manage.py migrate", "执行数据库迁移"):
        print("❌ 数据库迁移失败")
        return
    
    # 3. 创建示例数据
    print("\n📚 步骤3: 创建示例数据")
    if os.path.exists('create_sample_data.py'):
        if not run_command("python create_sample_data.py", "创建示例数据"):
            print("⚠️ 示例数据创建失败，但网站仍可正常运行")
    else:
        print("⚠️ 未找到示例数据脚本，跳过此步骤")
    
    # 4. 创建超级用户（可选）
    print("\n👤 步骤4: 创建超级用户")
    create_admin = input("是否创建超级用户？(y/n): ").lower().strip()
    if create_admin == 'y':
        run_command("python manage.py createsuperuser", "创建超级用户")
    
    # 5. 启动服务器
    print("\n🌐 步骤5: 启动开发服务器")
    print("✅ 所有准备工作完成！")
    print("\n📝 使用说明:")
    print("- 网站地址: http://127.0.0.1:8000")
    print("- 管理后台: http://127.0.0.1:8000/admin")
    print("- 按 Ctrl+C 停止服务器")
    print("\n🚀 正在启动服务器...")
    
    # 启动服务器
    try:
        subprocess.run("python manage.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")

if __name__ == '__main__':
    main() 