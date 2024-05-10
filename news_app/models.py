from django.db import models


class Viewer(models.Model):
    ipaddress = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.ipaddress

    class Meta:
        verbose_name = 'Viewer'
        verbose_name_plural = 'Viewers'


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='name')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class News(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='title')
    text = models.TextField(verbose_name='text')
    image = models.ImageField(upload_to='news', verbose_name='image', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='tags', related_name='news')
    viewers = models.ManyToManyField(Viewer, verbose_name='viewers', related_name='news', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
