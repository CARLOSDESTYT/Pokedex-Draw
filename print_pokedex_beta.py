import pandas as pd
import random

# DataBase
df_pokedex = pd.read_csv("D:\Pc\Programación\Python\Pokedex\pokedex_database_api.csv")

def elefir_filtro(opcion):
    match opcion:
        case 1:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Agua', na=False)]
            return df_filtrado
        case 2:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Fuego', na=False)]
            return df_filtrado
        case 3:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Planta', na=False)]
            return df_filtrado
        case 4:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Eléctrico', na=False)]
            return df_filtrado
        case 5:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Psíquico', na=False)]
            return df_filtrado
        case 6:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Lucha', na=False)]
            return df_filtrado
        case 7:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Oscuro', na=False)]
            return df_filtrado
        case 8:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Metálico', na=False)]
            return df_filtrado
        case 9:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Hada', na=False)]
            return df_filtrado
        case 10:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Dragón', na=False)]
            return df_filtrado
        case 11:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Volador', na=False)]
            return df_filtrado
        case 12:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Tierra', na=False)]
            return df_filtrado
        case 13:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Veneno', na=False)]
            return df_filtrado
        case 14:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Bicho', na=False)]
            return df_filtrado
        case 15:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Roca', na=False)]
            return df_filtrado
        case 16:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Fantasma', na=False)]
            return df_filtrado
        case 17:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Hielo', na=False)]
            return df_filtrado
        case 18:
            df_filtrado = df_pokedex[df_pokedex['Tipo'].str.contains('Normal', na=False)]
            return df_filtrado
        case _:
            return df_pokedex

# Obtener entrada del usuario
opcion = int(input('Elige un número del 0 al 18: '))
df_filtrado = elefir_filtro(opcion)

def get_random_poke_num(df):
    return random.choice(df['N'].values)

partes_cuerpo = {
    'cuerpo_superior': get_random_poke_num(df_filtrado),
    'cuerpo_inferior': get_random_poke_num(df_filtrado),
    'cabeza': get_random_poke_num(df_filtrado),
    'cola': get_random_poke_num(df_filtrado),
    'patas_traseras': get_random_poke_num(df_filtrado),
    'patas_delanteras': get_random_poke_num(df_filtrado),
    'ojos': get_random_poke_num(df_filtrado),
    'boca': get_random_poke_num(df_filtrado),
    'orejas': get_random_poke_num(df_filtrado),
    'detalles': get_random_poke_num(df_filtrado),
    'color': get_random_poke_num(df_filtrado)
}

# Función para buscar partes
def buscar_parte(numero):
    resultado = df_pokedex[df_pokedex['N'] == numero]
    return resultado.iloc[0] if not resultado.empty else None

# Construir el Pokémon combinado
pokemon_combinado = {}
for parte, numero in partes_cuerpo.items():
    pokemon_part = buscar_parte(numero)
    if pokemon_part is not None:
        pokemon_combinado[parte] = {
            'Número': numero,
            'Nombre': pokemon_part['Nombre'],
            'Tipo': pokemon_part['Tipo']
        }

# Mostrar resultados
print("\nPokémon Combinado:")
for parte, datos in pokemon_combinado.items():
    print(f"{parte.replace('_', ' ').title():<20} | N.° {datos['Número']:04} | {datos['Nombre']} ({datos['Tipo']})")