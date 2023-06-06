import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(f'/media/{pokemon.image}'),
            'title_ru': pokemon.title,
        })

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    now_time = localtime()
    for pokemon_entity in PokemonEntity.objects.filter(
                                                appeared_at__lt=now_time,
                                                disappeared_at__gt=now_time):
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(
                f'/media/{pokemon_entity.pokemon.image}'))

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    print(f'Pokemon ID: {pokemon_id}')
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if not pokemon:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    now_time = localtime()
    for pokemon_entity in PokemonEntity.objects.filter(
                                                pokemon=pokemon,
                                                appeared_at__lt=now_time,
                                                disappeared_at__gt=now_time):
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(
                f'/media/{pokemon_entity.pokemon.image}'))

    pokemon_on_page = {
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(f'/media/{pokemon.image}'),
            'title_ru': pokemon.title,
            'description': pokemon.description,
            'title_en': pokemon.title_en,
            'title_jp': pokemon.title_jp,
        }
    if pokemon.previous_evolution:
        print(f'Previous_evolution: {pokemon.previous_evolution}')
        pokemon_on_page['previous_evolution'] = {
                    'pokemon_id': pokemon.previous_evolution.id,
                    'img_url': request.build_absolute_uri(
                        f'/media/{pokemon.previous_evolution.image}'),
                    'title_ru': pokemon.previous_evolution.title,
                    }
    if pokemon.next_evolutions.exists():
        print(f'Next_evolution: {pokemon.next_evolutions}')
        next_evolution = pokemon.next_evolutions.first()
        pokemon_on_page['next_evolution'] = {
                    'pokemon_id': next_evolution.id,
                    'img_url': request.build_absolute_uri(
                        f'/media/{next_evolution.image}'),
                    'title_ru': next_evolution.title,
                }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })
