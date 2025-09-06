#!/usr/bin/env python3
"""
ملف إعداد مكتبة WOLF.py
"""

from setuptools import setup, find_packages
import os

# قراءة الإصدار من الملف
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'wolf_py', '__init__.py')
    with open(version_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"').strip("'")
    return "1.0.0"

# قراءة متطلبات المشروع
def get_requirements():
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return [
        'aiohttp>=3.8.0',
        'websockets>=10.0',
        'PyYAML>=6.0',
        'requests>=2.28.0'
    ]

# قراءة الوصف الطويل
def get_long_description():
    readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            return f.read()
    return """
# WOLF.py

مكتبة Python غير رسمية للاتصال بمنصة WOLF (المعروفة سابقاً باسم Palringo).

## الميزات
- دعم كامل لـ async/await
- نظام أوامر متقدم
- معالجة الأحداث والرسائل
- دعم اللغة العربية
- إدارة الإعدادات والترجمات

## التثبيت
```bash
pip install wolf-py
```

## الاستخدام
```python
from wolf_py import WOLFClient, Command

client = WOLFClient()
await client.login()
```
    """

setup(
    name="wolf-py",
    version=get_version(),
    author="WOLF.py Community",
    author_email="wolfpy@example.com",
    description="مكتبة Python غير رسمية للاتصال بمنصة WOLF",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/wolfpy-community/wolf-py",
    project_urls={
        "Bug Reports": "https://github.com/wolfpy-community/wolf-py/issues",
        "Source": "https://github.com/wolfpy-community/wolf-py",
        "Documentation": "https://wolf-py.readthedocs.io/",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=get_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "redis": [
            "redis>=4.0.0",
        ],
    },
    keywords=[
        "wolf", "palringo", "chat", "bot", "messaging", 
        "websocket", "async", "arabic", "python3"
    ],
    include_package_data=True,
    package_data={
        'wolf_py': [
            'config/*.yaml',
            'phrases/*.json',
            'examples/*.py',
        ],
    },
    entry_points={
        'console_scripts': [
            'wolf-py=wolf_py.examples.simple_bot:main',
        ],
    },
    zip_safe=False,
)