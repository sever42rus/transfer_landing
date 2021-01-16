from django.db import models
from ckeditor.fields import RichTextField

from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

from django.utils.safestring import mark_safe

# Create your models here.

class Services(models.Model):
	title = models.CharField(max_length=50, verbose_name='Заголовок',)
	short_description = models.TextField(verbose_name='Краткое описание',)
	full_description = RichTextField(verbose_name='Полное описание',)

	pictogram = models.ImageField(upload_to='services', verbose_name='Пиктограмма',)
	def image_pictogram(self):
		if self.pictogram:
			return mark_safe(u'<div align="center"><img src="{0}" height="40"/></a></div>'.format(self.pictogram.url))
		else:
			return 'Пиктограмма отсутствует.'
	image_pictogram.short_description = ' '

	class Meta:
		verbose_name_plural = 'Услуги'
		verbose_name = 'Услуга'

	def __str__(self):
		return self.title

class CarouselInner(models.Model):
	service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга',)
	title = models.CharField(max_length=30, verbose_name='Заголовок',)
	text = models.CharField(max_length=500, blank=True, null=True, verbose_name='Текст',)
	img = models.ImageField(upload_to='setting', verbose_name='Изображение',)
	img_mobile = ImageSpecField(source='img',
		processors=[Adjust(contrast=1.2, sharpness=1.2), ResizeToFill(800, 800)], 
		format='JPEG', 
		options={'quality': 90}
		)
	img_desktop = ImageSpecField(source='img',
		processors=[Adjust(contrast=1.2, sharpness=1.2), ResizeToFill(1920, 1080)], 
		format='JPEG', 
		options={'quality': 90}
		)

	def image_img(self):
		if self.img:
			return mark_safe(u'<div align="center"><img src="{0}" height="40"/></a></div>'.format(self.img.url))
		else:
			return 'Пиктограмма отсутствует.'
	image_img.short_description = ' '

	class Meta:
		verbose_name_plural = "Вкладки карусели"
		verbose_name = "Вкладка"

	def __str__(self):
		return self.title
