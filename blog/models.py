from django.db import models

class Article(models.Model):
    uid =- models.CharField('UID', max_length=6, null=False, blank=False)
    title = models.CharField('标题', max_length=128)
    body = models.TextField('正文')
    body_raw = models.TextField('正文_markdown')
    head_pic = models.CharField('题图', max_length=256)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    views_count = models.PositiveIntegerField('浏览量', default=0)

    class Meta:
        ordering = ('-created_time', )
