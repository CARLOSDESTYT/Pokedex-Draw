import requests
import pandas as pd
import os

def get_pokedex_from_api():
    # Configuración inicial
    pokedex_data = []

    # Rango de Pokémon a scrapear
    for pokemon_id in range(1, 1026):
        try:
            # Obtener datos del Pokémon
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
            pokemon = response.json()

            # Obtener datos de la especie para el número de Pokédex
            species_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/")
            species = species_response.json()

            # Extrar nombre/número/tipo/imagen_url del pokémon
            name = pokemon['name'].capitalize()
            number = str(species['id']).zfill(4)
            types = [t['type']['name'].capitalize() for t in pokemon['types']]
            image_url = pokemon['sprites']['other']['official-artwork']['front_default']

            # Descargar imagen
            if image_url:
                img_data =requests.get(image_url).content
                image_filename = f"pokemon_images/{number}_{name}.png"
                os.makedirs('pokemon_images', exist_ok=True)
                with open(image_filename, 'wb') as handler:
                    handler.write(img_data)

            # Añadir a la lista
            pokedex_data.append({
                'N.°': number,
                'Nombre': name,
                'Tipos': ', '.join(types),
                'IMG': image_filename if image_url else None
            })

            print(f"Pokémon: #{number} {name}")

        except Exception as e:
            print(f"Error al procesar Pokémon #{pokemon_id}: {str(e)}")
            continue
    # Guardar como CSV
    df = pd.DataFrame(pokedex_data)
    df.to_csv('pokedex_database_api.csv', index=False)
    print("Base de datos de la Pokédex creada con éxito usando PokeAPI!")

if __name__ == "__main__":
    get_pokedex_from_api()