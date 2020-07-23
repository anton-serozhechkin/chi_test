from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.utils import timezone

class Record(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    last_name = models.CharField('Фамилия', max_length=100, unique=True)
    country = CountryField('Страна', default='UA', blank=True, null=True)
    city = models.CharField('Город', max_length=100, blank=True, null=True)
    street = models.CharField('Улица', max_length=100, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Телефонный номер должен быть в формате: '+999999999'. Допускается до 15 цифр.")
    phone_number = models.CharField('Телефонный номер', validators=[phone_regex], max_length=17) # валидатор должен быть списком    URL (опциональное поле, с валидацией) 
    image = models.ImageField('Фотография', upload_to='images/%Y/%m/%h/', null=True, blank=True)
    created = models.DateTimeField('Запись добавлена', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    
    class Meta:
        verbose_name = 'Запись в адресной книге'
        verbose_name_plural = 'Записи в адресной книге'
    
    def __str__(self):
        if self.country:
            return 'Пользователь {} {} из {}.'.format(self.last_name, self.name, self.country.name)
        else:
            return 'Пользователь {} {}.'.format(self.last_name, self.name)

    #def get_absolute_url(self):
    #    return reverse('event_detail', kwargs={'slug': self.slug})