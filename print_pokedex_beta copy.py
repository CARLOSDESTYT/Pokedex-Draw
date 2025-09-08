import pandas as pd
import random
import tkinter as tk
import os
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Pokedex")

x = (root.winfo_screenwidth() - 500) // 2
y = int(root.winfo_screenwidth() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=500, height=600, bg="#2D478D")

# DataBase
df_pokedex = pd.read_csv("D:\Pc\Programación\Python\Pokedex\pokedex_database_api.csv")


# Menú
def mostrar_menu():
    print("\n--- Menú de Filtros Pokémon ---")
    print("1. Filtrar por tipo Agua")
    print("2. Filtrar por tipo Fuego")
    print("3. Filtrar por tipo Planta")
    print("4. Filtrar por tipo Eléctrico")
    print("5. Filtrar por tipo Psíquico")
    print("6. Filtrar por tipo Lucha")
    print("7. Filtrar por tipo Oscuro")
    print("8. Filtrar por tipo Metálico")
    print("9. Filtrar por tipo Hada")
    print("10. Filtrar por tipo Dragón")
    print("11. Filtrar por tipo Volador")
    print("12. Filtrar por tipo Tierra")
    print("13. Filtrar por tipo Veneno")
    print("14. Filtrar por tipo Bicho")
    print("15. Filtrar por tipo Roca")
    print("16. Filtrar por tipo Fantasma")
    print("17. Filtrar por tipo Hielo")
    print("18. Filtrar por tipo Normal")
    print("0. No filtrar (mostrar todos)")
    print("99. Salir")

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

# Manda a pedirn un número aleatorio según el filtro
def get_random_poke_num(df_filtrado):
    return random.choice(df_filtrado['N.'].values)

# Función para buscar partes
def buscar_parte(numero):
    resultado = df_pokedex[df_pokedex['N.'] == numero]
    return resultado.iloc[0] if not resultado.empty else None


# Programa principal
while True:
    mostrar_menu()
    try:
        opcion = int(input('Elige un número del 0 al 18: '))

        if opcion == 99:
            print("Saliendo del programa...")
            break
        
        df_filtrado = elefir_filtro(opcion)

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

        # Construir el Pokémon combinado
        pokemon_combinado = {}
        for parte, numero in partes_cuerpo.items():
            pokemon_part = buscar_parte(numero)
            if pokemon_part is not None:
                pokemon_combinado[parte] = {
                    'Número': numero,
                    'Nombre': pokemon_part['Nombre'],
                    'Tipo': pokemon_part['Tipo'],
                    'IMG': pokemon_part['IMG']
                }
        


        # Mostrar resultados
        for parte, datos in pokemon_combinado.items():
            lista_imagenes = []
            lista_tipos = []
            lista_nombres = []

            for parte, datos in pokemon_combinado.items():
                print(f"{parte.replace('_', ' ').title():<20} | N.° {datos['Número']:04} | {datos['Nombre']} ({datos['Tipo']})")
                lista_imagenes.append(datos['IMG'])
                lista_tipos.append(datos['Tipo'])
                lista_nombres.append(datos['Nombre'])

            current_image_index = 0

            def mostrar_imagen(index):
                global imagen_tk, etiqueta_imagen, etiqueta_tipo, etiqueta_nombre
                
                try:
                    # Limpiar widgets anteriores
                    for widget in [etiqueta_imagen, etiqueta_tipo, etiqueta_nombre, error_label]:
                        if widget and widget.winfo_exists():
                            widget.pack_forget()
                    
                    ruta_imagen = os.path.join(os.path.dirname(__file__), lista_imagenes[index].replace('/', os.sep))
                    
                    # Abrir la imagen con PIL
                    imagen_pil = Image.open(ruta_imagen)
                    imagen_tk = ImageTk.PhotoImage(imagen_pil)
                    
                    etiqueta_imagen = tk.Label(root, image=imagen_tk)
                    etiqueta_imagen.pack()

                    etiqueta_nombre = tk.Label(root, text=lista_nombres[index], font=('Arial', 14, 'bold'))
                    etiqueta_nombre.pack()
                    
                    etiqueta_tipo = tk.Label(root, text=f"Tipo: {lista_tipos[index]}", font=('Arial', 12))
                    etiqueta_tipo.pack()
                    
                except Exception as e:
                    error_msg = f"No se pudo cargar la imagen: {str(e)}"
                    print(error_msg)
                    error_label = tk.Label(root, text=error_msg, fg="red")
                    error_label.pack()

            def siguiente_imagen():
                global current_image_index
                if current_image_index < len(lista_imagenes) - 1:
                    current_image_index += 1
                    mostrar_imagen(current_image_index)

            def anterior_imagen():
                global current_image_index
                if current_image_index > 0:
                    current_image_index -= 1
                    mostrar_imagen(current_image_index)

            # Mostrar la primera imagen
            mostrar_imagen(current_image_index)

            # Frame para los botones
            frame_botones = tk.Frame(root)
            frame_botones.pack(pady=15)

            # Botón anterior
            boton_anterior = tk.Button(frame_botones, text="Anterior", command=anterior_imagen)
            boton_anterior.pack(side=tk.LEFT, padx=5)

            # Botón siguiente
            boton_siguiente = tk.Button(frame_botones, text="Siguiente", command=siguiente_imagen)
            boton_siguiente.pack(side=tk.LEFT, padx=5)

            root.mainloop()
        
    # En caso de error
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
