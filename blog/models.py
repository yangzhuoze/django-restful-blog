from django.db import models

from common.utils.generate import uid_generate
from common.utils.renderers import markdown


class Config(models.Model):
    key = models.CharField('键', max_length=64, null=False, blank=False, unique=True)
    value = models.CharField('值', max_length=255, null=False)


class Article(models.Model):
    uid = models.CharField('UID', max_length=8, default=uid_generate, editable=False, unique=True)
    title = models.CharField('标题', max_length=128)
    body = models.TextField('正文')
    body_raw = models.TextField('正文_markdown')
    created_time = models.DateTimeField('创建时间', auto_now_add=True, editable=False)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    views_count = models.PositiveIntegerField('浏览量', default=0)

    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='标签')

    class Meta:
        ordering = ('-created_time',)

    def save(self, *args, **kwargs):
        self.body = markdown(self.body_raw)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField('标签名', max_length=32, unique=True)

    def __str__(self):
        return self.name
