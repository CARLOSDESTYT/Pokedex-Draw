import csv
import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'draw_pokemon.settings')
django.setup()

from pokedex.models import Pokemon

def importar_datos():
    ruta_csv = 'pokedex_database_api.csv'
    
    with open(ruta_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Pokemon.objects.get_or_create(
                numero=int(row['N.°']),
                nombre=row['Nombre'],
                tipos=row['Tipos'],
                img_path=row['IMG']
            )
    print("¡Datos importados con éxito!")

if __name__ == '__main__':
    importar_datos()