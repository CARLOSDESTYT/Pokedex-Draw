from django.shortcuts import render, get_object_or_404
from .models import Pokemon
import random


def index(request):
    tipos = [
        "TODOS", "Normal","Fire","Water","Electric","Grass","Ice",
        "Fighting","Poison","Ground","Flying","Psychic",
        "Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"
    ]

    tipo = request.GET.get('tipo')
    nav = request.GET.get('nav')

    if tipo in tipos:
        idx = tipos.index(tipo)
    else:
        idx = 0

    columnas = 2
    filas = (len(tipos) + 1) // columnas

    if nav == "down":
        idx = (idx + columnas) % len(tipos)

    elif nav == "up":
        idx = (idx - columnas) % len(tipos)

    elif nav == "right":
        # solo si no está en la última columna
        if idx % columnas < columnas - 1 and idx + 1 < len(tipos):
            idx += 1

    elif nav == "left":
        # solo si no está en la primera columna
        if idx % columnas > 0:
            idx -= 1

    tipo_seleccionado = tipos[idx]

    return render(request, 'index.html', {
        'tipos': tipos,
        'tipo_seleccionado': tipo_seleccionado
    })


def pokemon(request):
    # 🔥 1. Estado desde URL
    tipo_seleccionado = request.GET.get('tipo', 'TODOS')
    index = int(request.GET.get('index', 0))
    seed = request.GET.get('seed', str(random.randint(1, 9999)))

    # 🔥 2. Filtrado
    if tipo_seleccionado and tipo_seleccionado != "TODOS":
        queryset = Pokemon.objects.filter(tipos__icontains=tipo_seleccionado)
    else:
        queryset = Pokemon.objects.all()

    lista_pokemons = list(queryset)

    if not lista_pokemons:
        return render(request, 'index.html', {
            'error': 'No se encontraron Pokémon'
        })

    # 🔥 3. Generar 11 Pokémon fijos
    random.seed(seed)
    cantidad = min(11, len(lista_pokemons))
    pokemons_random = random.sample(lista_pokemons, cantidad)

    # 🔥 4. Lista de partes
    partes = [
        "cabeza",
        "ojos",
        "boca",
        "orejas",
        "cuerpo superior",
        "cuerpo inferior",
        "patas delanteras",
        "patas traseras",
        "cola",
        "detalles",
        "color"
    ]

    # 🔥 5. Seguridad del índice
    index = max(0, min(index, cantidad - 1))

    pokemon_actual = pokemons_random[index]
    parte_actual = partes[index]

    # 🔥 6. Contexto
    return render(request, 'pokemon.html', {
        'pokemon': pokemon_actual,
        'pokemons': pokemons_random,
        'parte': parte_actual,
        'index': index,
        'tipo': tipo_seleccionado,
        'seed': seed,
        'prev_index': max(0, index - 1),
        'next_index': min(cantidad - 1, index + 1),
    })