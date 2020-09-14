from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=150)
    text = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL поста')
    img = models.ImageField(upload_to='post_pictures', default='default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(default=timezone.now)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    time_of_last_update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('getpost', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_of_creation']
