from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200)
    title_en = models.CharField('Название анг.', max_length=200, blank=True)
    title_jp = models.CharField('Название яп.', max_length=200, blank=True)
    image = models.ImageField('Картинка', null=True)
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey(
            'self',
            verbose_name='Из кого эволюционирует',
            on_delete=models.SET_NULL,
            related_name='next_evolutions',
            null=True,
            blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        on_delete=models.CASCADE,
        related_name='entities',
        )

    lat = models.FloatField('Координаты, широта')
    lon = models.FloatField('Координаты, долгота')

    appeared_at = models.DateTimeField(
        verbose_name='Время оживления',
        blank=True)
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения',
        blank=True)

    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Атака', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return 'Pokemon: {}, lat: {}, lon: {}'.format(
            self.pokemon.title, self.lat, self.lon)
