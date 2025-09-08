import requests
from bs4 import BeautifulSoup
import os

def scrape_pokedex():
    # Configuración inicial
    base_url = "https://www.pokemon.com/us/pokedex/"
    pokedex_data = []
    
    # Rango de Pokémon a scrapear (del 1 al 898 para la generación actual)
    for pokemon_id in range(1, 5):
        try:
            url = f"{base_url}{pokemon_id}"
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')

            print(soup)
            
            # Extraer nombre
            name = soup.find('div', class_='pokedex-pokemon-pagination-title').text.split()[0]
            
            # Extraer número
            number = soup.find('div', class_='pokemon-number').text.strip()
            
            # Extraer tipos
            types = [typ.text.strip() for typ in soup.find_all('a', class_='dtm-type')]
            
            # Extraer imagen
            image_url = soup.find('div', class_='pokemon-image').find('img')['src']
            
            # Descargar imagen
            img_data = requests.get(image_url).content
            image_filename = f"pokemon_images/{number}_{name}.png"
            os.makedirs('pokemon_images', exist_ok=True)
            with open(image_filename, 'wb') as handler:
                handler.write(img_data)
            
            # Añadir datos a la lista
            pokedex_data.append({
                'number': number,
                'name': name,
                'types': ', '.join(types),
                'image_path': image_filename
            })
            
            print(f"Procesado: #{number} {name}")
            
        except Exception as e:
            print(f"Error al procesar Pokémon #{pokemon_id}: {str(e)}")
            continue
    

if __name__ == "__main__":
    scrape_pokedex()