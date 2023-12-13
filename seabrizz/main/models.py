from django.db import models


class SeaFood(models.Model):
    name = models.CharField('Наименование', max_length=75)
    proiz = models.CharField('Производиьтель', max_length= 75)
    price = models.CharField('Цена', max_length=75)
    descr = models.TextField('Описание')
    photo = models.ImageField(upload_to='images/')
    quantity = models.IntegerField('Количество', default=0)
    objects = models.Manager()
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
# Create your models here.
