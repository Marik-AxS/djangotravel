from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    image = models.ImageField('Картинка', upload_to='about_us')
    text1 = models.TextField('Текст 1')
    title2 = models.CharField('Почему мы', max_length=50)
    text2 = models.TextField('Текст 2')
    title3 = models.CharField('Наши преимущества', max_length=50)
    text3 = models.TextField('Текст 3')
    title4 = models.CharField('Наши услуги', max_length=50)
    text4 = models.TextField('Текст 4')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О насы'

class ContactUs(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.CharField('Email')
    phone = models.CharField('Телефон', max_length=50)
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

class Contacts(models.Model):
    number = models.CharField('Номер', max_length=50)
    email = models.CharField('Почта', max_length=50)
    address = models.CharField('Адрес', max_length=50)

    class Meta:
        verbose_name = 'Контактный'
        verbose_name_plural = 'Контактная'