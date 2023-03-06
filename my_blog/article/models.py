from django.db import models
# 导入内建的user模型
# django本身具有一个简单完整的账号系统（user）
# 足以满足一般网站的账号申请、建立、权限、群组等基本功能
from django.contrib.auth.models import User
# timezone用于处理时间相关事务
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# 处理图片
from PIL import Image

class ArticleColumn(models.Model):
    """
    栏目的model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    # created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。
    # 参数on_delete用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。
    # models.CharField为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 文章正文。
    # 保存大量文本使用TextField
    body = models.TextField()

    # 文章创建时间。
    # 参数default = timezone.now()指定其在创建数据时，默认写入当前的时间
    # created = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    # 文章更新时间。
    # 参数auto_now=True指定每次数据更新时，自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    total_views = models.PositiveIntegerField(default=0)
    """
    PositiveIntegerField是用于存储正整数的字段
    default=0设定初始值从0开始
    """
    # 文章栏目的“一对多”外键
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )

    # 文章标签
    tags = TaggableManager(blank=True)

    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)

    # 内部类class Meta用于给model定义元数据
    class Meta:
        # ordering指定模型返回的数据的排列顺序
        # ‘-created’表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数__str__定义当调用对象的str()方法时的返回值内容
    def __str__(self):
        # return self.title将文章标题返回
        return self.title
    
    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
    
    # 保存时处理图片
    def save(self, *args, **kwargs):
        # 调用原有的save()的功能
        article = super(ArticlePost, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article
    
    def  was_created_recently(self):
        # 若文章是最近发表的，则返回true
        diff = timezone.now() - self.created
        if diff.days == 0 and diff.days <= 0 and diff.seconds < 60:
            return True
        else:
            return False



    


