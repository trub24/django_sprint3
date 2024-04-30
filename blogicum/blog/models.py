from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class CoreBlogeModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class Location(CoreBlogeModel):
    name = models.CharField('Название места', max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(CoreBlogeModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'),
        unique=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(CoreBlogeModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор публикации')
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=('Если установить дату и время в '
                   'будущем — можно делать отложенные публикации.')
    )
    location = models.ForeignKey(Location, null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Местоположение')
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Категория')

    class Meta:
        default_related_name = 'post'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title
