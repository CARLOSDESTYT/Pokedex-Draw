# 🎨 Pokedex Draw - Proyecto Final (Bases de Datos V0718)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23336791.svg?style=for-the-badge&logo=postgresql&logoColor=white)

*Pokedex Draw* es una aplicación web interactiva diseñada bajo la estética retro de una GameBoy Color. El sistema permite a los usuarios filtrar Pokémon para el reto de “dibujar por partes”, facilitando una dinámica de aprendizaje artístico organizada mediante una base de datos relacional.

---

## 🧠 Enunciado del Problema
El proyecto resuelve la falta de una herramienta que organice y asigne aleatoriamente partes del cuerpo de distintos Pokémon para retos de dibujo. La base de datos permite filtrar por tipo, consultar datos técnicos y asegurar que la asignación de partes sea consistente mediante el uso de "seeds".

---

## 🚀 Funcionalidades
*   **Visualización Dinámica**: Selección de Pokémon aleatorios basados en un "seed" para asegurar consistencia en el dibujo por partes.
*   **Filtro por Tipo**: Navegación a través de los 18 tipos elementales mediante parámetros de URL.
*   **Simulación de Consola**: Interfaz interactiva que emula los controles de una GameBoy.

**Botones:**
*    **Flechas**: Moverse por el menú selección
*    **Select**: Entrar al menú selección
*    **Start**: Iniciar lista o reiniciarla
*    **A**: Siguiente pokemon
*    **B**: Anterior pokemon

<img width="1366" height="720" alt="Screenshot 2026-05-06 074002" src="https://github.com/user-attachments/assets/15fa01dc-beb3-4838-85e4-79e9eabffd77" />
<img width="1366" height="720" alt="Screenshot 2026-05-06 073937" src="https://github.com/user-attachments/assets/346af5a3-4c26-4fcc-9b47-fa0f1a2f65f7" />
<img width="1366" height="720" alt="Screenshot 2026-05-06 074110" src="https://github.com/user-attachments/assets/3da43b5e-1556-48d0-987a-6c0586bcfe6c" />

#### CRUD
El sistema implementa un ciclo completo de gestión de datos (CRUD) sobre PostgreSQL:
*   **Create**: Registro de nuevos Pokémon y usuarios artistas en la base de datos.
*   **Read**: Consulta filtrada por tipos elementales y visualización de detalles técnicos.
*   **Update**: Actualización de información de Pokémon (nombres, imágenes) y perfiles de usuario.
*   **Delete**: Eliminación de registros obsoletos o erróneos para mantener la integridad de la Pokedex.

---

## 📊 Diseño de la Base de Datos

### Modelo Entidad Relación (MER)
Representación lógica de las 5 tablas y sus interconexiones.
<img width="795" height="993" alt="image" src="https://github.com/user-attachments/assets/eadfff45-295c-495f-b52f-373fc148631f" />

### Modelo Relacional
Estructura técnica de tablas con llaves primarias (PK) y foráneas (FK).
<img width="854" height="977" alt="image" src="https://github.com/user-attachments/assets/d503e44e-ab38-4a7f-a244-94743a8f61d7" />

### 📂 Ver Diccionario de Datos Detallado

1. **Pokemon**: Almacena la información principal de cada Pokémon, incluyendo su número en la Pokédex, nombre, ruta de imagen y el usuario que lo gestiona.
2. **Tipos**: Contiene el catálogo de tipos elementales (Fuego, Agua, Planta, etc.).
3. **Pokemon_Tipos**: Tabla intermedia que gestiona la relación muchos a muchos entre Pokémon y tipos, ya que un Pokémon puede tener uno o varios tipos.
4. **Partes_Cuerpo**: Registra las diferentes partes de cada Pokémon (Cabeza, Ojos, Cola, etc.), asociadas a un Pokémon específico.
5. **Usuarios**: Almacena la información de los usuarios (entrenadores o artistas) que gestionan los registros de Pokémon.

### 1. Tabla: `Pokemon`
| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | ID único autoincremental. |
| `numero` | INT | NOT NULL, UNIQUE | Número oficial de la Pokédex. |
| `nombre` | VARCHAR(100) | NOT NULL | Nombre de la especie. |
| `img_path` | VARCHAR(255) | NOT NULL | Ruta de la imagen retro. |
| `usuario_id`| INT | FOREIGN KEY | Usuario que gestiona el registro. |

### 2. Tabla: `Tipos`
| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | ID único del tipo. |
| `nombre` | VARCHAR(50) | NOT NULL, UNIQUE | Ejemplo: Fire, Water, Ghost. |

### 3. Tabla: `Pokemon_Tipos` (Relación N:M)
Resuelve la relación muchos a muchos entre Pokémon y sus elementos.

### 4. Tabla: `Partes_Cuerpo`
| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | ID de la parte. |
| `nombre_parte`| VARCHAR(50) | NOT NULL | Cabeza, Ojos, Cola, etc. |
| `pokemon_id`| INT | FOREIGN KEY | Pokémon asociado a esta parte. |

### 5. Tabla: `Usuarios`
| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | ID del artista. |
| `nombre_usuario`| VARCHAR(50) | NOT NULL, UNIQUE | Nombre de perfil. |


---

## 💾 Implementación y Respaldo
La base de datos está normalizada en **PostgreSQL**. 

*   **Consultas con JOIN**: El sistema utiliza `SELECT` con `JOIN` para vincular los Pokémon con sus respectivos tipos y partes del cuerpo.
*   **Respaldo**: Se incluye un archivo de respaldo en texto plano generado con:
    ```bash
    pg_dump -U postgres -d pokedex_draw > backup_pokedex.sql
    ```

---

## 🛠️ Tecnologías Utilizadas

- Python 3.11.9 🐍
- Django 🌐
- HTML / CSS
- PokéAPI
- PostgreSQL

---

## 🚀 Instalación y Uso

### 1. Clonar repositorio
git clone https://github.com/CARLOSDESTYT/Pokedex-Draw.git
cd Pokedex-Draw

### 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Migraciones
python manage.py migrate

### 5. Ejecutar servidor
python manage.py runserver

### 6. Entrar a la página a través de tu navegador
http://127.0.0.1:8000
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt



