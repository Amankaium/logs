from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(verbose_name="Текст статьи")
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True, null=True,
        
    )
    publicated = models.BooleanField(default=True)
    
    short_description = models.TextField(
        null=True, blank=True,
        verbose_name="Краткое описание"
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=False,
        verbose_name="Автор",
        related_name="created_article"
    )

    readers = models.ManyToManyField(
        to=User,
        blank=True,
        verbose_name="Читатели",
        related_name="readed_article"
    )

    rating = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )




class Profile(models.Model):
    vk = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Страница ВКонтакте"
    )

    fb = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Страница в Facebook"
    )

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="profile"
    )

    photo = models.ImageField(
        null=True, blank=True,
        upload_to="profiles"
    )