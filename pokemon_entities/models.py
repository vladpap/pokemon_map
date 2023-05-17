from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)


    def __str__(self):
        return'Pokemon: {}, lat: {}, lon: {}'.format(
            self.pokemon.title, self.lat, self.lon)
