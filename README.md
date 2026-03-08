# Sistema de Gestión de Biblioteca Digital

Sistema de gestión de biblioteca digital desarrollado con Programación Orientada a Objetos y arquitectura por capas.

## 📁 Estructura del Proyecto

```
biblioteca_app/
│
├── modelos/
│   ├── __init__.py
│   ├── libro.py          # Entidad Libro
│   └── usuario.py        # Entidad Usuario
│
├── servicios/
│   ├── __init__.py
│   └── biblioteca_servicio.py  # Lógica de negocio
│
├── main.py               # Punto de entrada
└── README.md             # Este archivo
```

## 🏗️ Arquitectura por Capas

### Capa de Modelos (`modelos/`)
Contiene las clases que representan las entidades del sistema:

- **Libro**: Representa un libro con:
  - ISBN (identificador único)
  - Título y Autor almacenados en **tupla** (inmutable)
  - Categoría

- **Usuario**: Representa un usuario con:
  - ID único
  - Nombre
  - Lista de libros prestados (**lista** - colección dinámica)

### Capa de Servicios (`servicios/`)
Contiene la lógica de negocio:

- **BibliotecaServicio**: Gestiona:
  - **Diccionario** de libros disponibles (ISBN → Libro) - búsqueda O(1)
  - **Diccionario** de usuarios registrados (ID → Usuario)
  - **Conjunto** (set) de IDs de usuarios - garantiza unicidad

### Punto de Entrada (`main.py`)
- Menú interactivo en consola
- No contiene lógica de negocio
- Delega todas las operaciones al servicio

## 🚀 Ejecución

```bash
# Navegar al directorio del proyecto
cd biblioteca_app

# Ejecutar el sistema
python main.py
```

## 📋 Funcionalidades

### Gestión de Libros
- ✅ Agregar libro
- ✅ Quitar libro
- ✅ Buscar por título
- ✅ Buscar por autor
- ✅ Buscar por categoría
- ✅ Listar todos los libros

### Gestión de Usuarios
- ✅ Registrar usuario
- ✅ Dar de baja usuario
- ✅ Listar usuarios

### Préstamos
- ✅ Prestar libro
- ✅ Devolver libro
- ✅ Listar libros prestados por usuario

### Estadísticas
- ✅ Ver estadísticas del sistema

## 💻 Uso

Al iniciar el sistema, se mostrará un menú interactivo:

```
==================================================
  SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
==================================================

--- GESTIÓN DE LIBROS ---
1.  Agregar libro
2.  Quitar libro
3.  Buscar libro por título
4.  Buscar libro por autor
5.  Buscar libro por categoría
6.  Listar todos los libros

--- GESTIÓN DE USUARIOS ---
7.  Registrar usuario
8.  Dar de baja usuario
9.  Listar usuarios

--- PRÉSTAMOS ---
10. Prestar libro
11. Devolver libro
12. Listar libros prestados a un usuario

--- ESTADÍSTICAS ---
13. Ver estadísticas del sistema

0.  Salir
```

## 🔧 Tecnologías Utilizadas

- **Python 3.8+**
- **Colecciones**:
  - `tuple` - para datos inmutables (título, autor)
  - `list` - para colecciones dinámicas (libros prestados)
  - `dict` - para búsquedas eficientes O(1)
  - `set` - para garantizar unicidad de IDs

## 📚 Decisiones de Diseño

1. **Tupla para título y autor**: Datos inmutables que no cambian, más eficiente en memoria
2. **Lista para libros prestados**: Colección dinámica que cambia con préstamos/devoluciones
3. **Diccionario para libros**: Búsqueda O(1) por ISBN
4. **Set para IDs**: Verificación de unicidad en O(1)
5. **Encapsulamiento**: Atributos privados con properties para control de acceso
6. **Separación de responsabilidades**: Modelos solo datos, Servicio lógica, Main interfaz

## 👨‍💻 Autor

Desarrollado como parte de la Semana 12 - Programación Orientada a Objetos
