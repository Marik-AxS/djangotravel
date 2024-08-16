from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('слаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField('Название тега', max_length=100)
    slug = models.SlugField('слаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Post(models.Model):
    title = models.CharField('Название поста', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField('Изображение', upload_to='posts')
    like = models.PositiveIntegerField('Количество лайков', default=0)
    text = models.TextField('Текст поста')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

