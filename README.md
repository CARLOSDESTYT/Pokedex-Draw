# 🎨 Pokedex Draw - Proyecto Final (Bases de Datos V0718)

**Pokedex Draw** es una aplicación web interactiva diseñada bajo la estética retro de una GameBoy Color. El sistema permite a los usuarios gestionar información de Pokémon para utilizarlos como referencia visual al "dibujar por partes", facilitando la creación de nuevos diseños basados en anatomías existentes.

## 📊 Cumplimiento de Rúbrica

[cite_start]Este proyecto ha sido desarrollado siguiendo estrictamente los requisitos de la materia[cite: 4, 7]:

* [cite_start]**Diseño de DB:** Incluye Modelo Entidad-Relación, Modelo Relacional y Diccionario de Datos[cite: 10, 34].
* [cite_start]**Implementación:** Base de datos robusta en **PostgreSQL**[cite: 22].
* [cite_start]**Normalización:** 5 tablas relacionadas en su totalidad y normalizadas[cite: 12, 16, 17].
* [cite_start]**Relaciones:** Implementación de llaves primarias, foráneas y una relación **Muchos a Muchos**[cite: 18, 22].
* [cite_start]**Interfaz Gráfica:** Sistema funcional que permite realizar operaciones **CRUD** (Create, Read, Update, Delete)[cite: 27].
* [cite_start]**Consultas Avanzadas:** Uso de sentencias `SELECT` con `JOIN` para la visualización de datos interrelacionados[cite: 24].

---

## 🧠 Enunciado del Problema
El proyecto busca resolver la falta de una herramienta organizada para artistas que necesitan referencias anatómicas específicas de Pokémon. [cite_start]La base de datos permite filtrar especies por tipo y consultar un desglose detallado de sus partes (Cabeza, Cuerpo, Extremidades, etc.) para facilitar el proceso creativo[cite: 9, 10, 32].

---

## 🛠️ Tecnologías Utilizadas
- [cite_start]**Lenguaje:** Python 3.x[cite: 28].
- [cite_start]**Framework Web:** Django[cite: 28].
- [cite_start]**Base de Datos:** PostgreSQL[cite: 22].
- **Estilos:** CSS3 con Google Fonts (VT323/Inter).
- **Entorno:** Virtualenv.

---

## 📂 Estructura de la Base de Datos (5 Tablas)
[cite_start]Para cumplir con la rúbrica, la base de datos se estructura de la siguiente manera[cite: 12]:
1.  [cite_start]**Pokemon**: Almacena el nombre, número y ruta de imagen[cite: 13, 32].
2.  [cite_start]**Partes_Cuerpo**: Tabla con las etiquetas detalladas (Cabeza, Cola, Ojos, etc.)[cite: 13].
3.  **Tipos**: Catálogo de tipos elementales (Fuego, Agua, Planta, etc.).
4.  [cite_start]**Pokemon_Tipos**: Tabla intermedia para la relación **Muchos a Muchos**[cite: 18].
5.  **Usuarios**: Registro de entrenadores/artistas que gestionan la base de datos.

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
