"""
Módulo BibliotecaServicio - Capa de servicio con la lógica de negocio.

Este módulo define la clase BibliotecaServicio que gestiona toda la lógica
del sistema de biblioteca digital. Implementa el patrón de arquitectura por
capas separando claramente la lógica de negocio de los modelos.

Decisiones de diseño:
- Diccionario para libros disponibles: clave=ISBN, valor=Objeto Libro
  Permite búsquedas O(1) por ISBN, muy eficiente.
- Diccionario para usuarios: clave=ID usuario, valor=Objeto Usuario
  Permite acceso directo a usuarios por su ID.
- Conjunto (set) para IDs de usuarios: garantiza unicidad y verificación
  de existencia en O(1).
- Se implementan validaciones para mantener la integridad de los datos.
"""

from modelos import Libro
from modelos import Usuario

class BibliotecaServicio:
    """
    Servicio Biblioteca (lógica de negocio).
    
    Gestiona las operaciones de la biblioteca digital, interactuando con
    los modelos de datos para realizar acciones como prestar y devolver libros.
    
    Atributos:
        __libros_disponibles (dict): Diccionario de libros disponibles (ISBN -> Libro)
        __usuarios (dict): Diccionario de usuarios registrados (ID usuario -> Usuario)
        __ids_usuarios (set): Conjunto de IDs de usuarios para verificación rápida
    """
    def __init__(self):
        """Inicializa el servicio con estructuras de datos vacías."""
        self.__libros_disponibles = {}  # ISBN -> Libro
        self.__usuarios = {}  # ID usuario -> Usuario
        self.__ids_usuarios = set()  # Conjunto para IDs de usuarios
    
    # =====================
    # GESTIÓN DE LIBROS
    # =====================

    def agregar_libro(self, isbn: str, titulo: str, autor: str, categoria: str) -> Libro:
        """
        Agrega un nuevo libro a la biblioteca.
        
        Args:
            isbn: ISBN único del libro
            titulo: Título del libro
            autor: Autor del libro
            categoria: Categoría del libro
        
        Returns:
            El objeto Libro agregado.
        
        Raises:
            ValueError: Si el ISBN ya existe en la biblioteca.
        """
        isbn = (isbn or "").strip()
        titulo = (titulo or "").strip()
        autor = (autor or "").strip()
        categoria = (categoria or "").strip()

        if not isbn or not titulo or not autor:
            raise ValueError("ISBN, título y autor son obligatorios.")
        

        libro = Libro(isbn, titulo, autor, categoria)
        self.__libros_disponibles[isbn] = libro
        return libro

    def quitar_libro(self, isbn: str) -> None:
        """
        Elimina un libro del catálogo.
        
        Args:
            isbn: ISBN del libro a eliminar
            
        Raises:
            ValueError: Si el libro no existe o está prestado
        """
        isbn = (isbn or "").strip()

        if isbn not in self.__libros_disponibles:
            raise ValueError(f"No existe un libro con el ISBN '{isbn}'.")

        # Verificar si algún usuario tiene el libro prestado
        for usuario in self.__usuarios.values():
            if usuario.tiene_libro(isbn):
                raise ValueError(f"No se puede eliminar: el libro está prestado a {usuario.nombre}.")

        del self.__libros_disponibles[isbn]

    def obtener_libro(self, isbn: str) -> Libro | None:
        """
        Obtiene un libro por su ISBN.
        
        Args:
            isbn: ISBN del libro a obtener
            
        Returns:
            El objeto Libro si se encuentra, o None si no existe.
        """
        isbn = (isbn or "").strip()
        return self.__libros_disponibles.get(isbn)

    def listar_libros(self) -> list[Libro]:
        """
        Retorna todos los libros del catálogo.
        
        Returns:
            list: Lista de todos los libros
        """
        return list(self.__libros_disponibles.values())

    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        """
        Busca libros por título (búsqueda parcial, case-insensitive).
        
        Args:
            titulo: Título o parte del título a buscar
            
        Returns:
            list: Lista de libros que coinciden
        """
        titulo_busqueda = titulo.lower().strip() # Comprensión de lista para filtrar eficientemente
        return [libro for libro in self.__libros_disponibles.values()
                if titulo_busqueda in libro.titulo.lower()]

    def buscar_por_autor(self, autor: str) -> list[Libro]:
        """
        Busca libros por autor (búsqueda parcial, case-insensitive).
        
        Args:
            autor: Autor o parte del nombre a buscar
            
        Returns:
            list: Lista de libros que coinciden
        """
        autor_busqueda = autor.lower().strip() # Comprensión de lista para filtrar eficientemente
        
        return [libro for libro in self.__libros_disponibles.values() 
                if autor_busqueda in libro.autor.lower()]

    def buscar_por_categoria(self, categoria: str) -> list[Libro]:
        """
        Busca libros por categoría (búsqueda parcial, case-insensitive).
        
        Args:
            categoria: Categoría o parte de ella a buscar
            
        Returns:
            list: Lista de libros que coinciden
        """
        categoria_busqueda = categoria.lower().strip()
        # Comprensión de lista para filtrar eficientemente
        return [libro for libro in self.__libros_disponibles.values() 
                if categoria_busqueda in libro.categoria.lower()]

    # =====================
    # GESTIÓN DE USUARIOS
    # =====================

    def registrar_usuario(self, id_usuario: str, nombre: str) -> Usuario:
        """
        Registra un nuevo usuario en la biblioteca.
        
        Args:
            id_usuario: ID único del usuario
            nombre: Nombre del usuario
            
        Returns:
            El objeto Usuario registrado.
            
        Raises:
            ValueError: Si el ID ya existe o es inválido
        """
        id_usuario = (id_usuario or "").strip()
        nombre = (nombre or "").strip()

        if not id_usuario or not nombre:
            raise ValueError("ID de usuario y nombre son obligatorios.")

        if id_usuario in self.__ids_usuarios:
            raise ValueError(f"Ya existe un usuario con el ID '{id_usuario}'.")

        usuario = Usuario(id_usuario, nombre)
        self.__usuarios[id_usuario] = usuario
        self.__ids_usuarios.add(id_usuario)
        return usuario

    def eliminar_usuario(self, id_usuario: str) -> None:
        """
        Elimina un usuario registrado.
        
        Args:
            id_usuario: ID del usuario a eliminar
            
        Raises:
            ValueError: Si el usuario no existe o tiene libros prestados
        """
        id_usuario = (id_usuario or "").strip()

        if id_usuario not in self.__ids_usuarios:
            raise ValueError(f"No existe un usuario con el ID '{id_usuario}'.")

        usuario = self.__usuarios[id_usuario]

        if usuario.libros_prestados:
            raise ValueError(f"No se puede eliminar: el usuario tiene libros prestados.")

        del self.__usuarios[id_usuario]
        self.__ids_usuarios.remove(id_usuario)
    
    def obtener_usuario(self, id_usuario: str) -> Usuario | None:
        """
        Obtiene un usuario por su ID.
        
        Args:
            id_usuario: ID del usuario
            
        Returns:
            Usuario: El usuario encontrado o None
        """
        return self.__usuarios.get(id_usuario.strip())

    def listar_usuarios(self) -> list[Usuario]:
        """
        Retorna todos los usuarios registrados.
        
        Returns:
            list: Lista de todos los usuarios
        """
        return list(self.__usuarios.values())

    def existe_usuario(self, id_usuario: str) -> bool:
        """
        Verifica si existe un usuario con el ID dado.
        
        Args:
            id_usuario: ID a verificar
            
        Returns:
            bool: True si el usuario existe
        """
        return id_usuario.strip() in self.__ids_usuarios

    # =====================
    # PRÉSTAMOS Y DEVOLUCIONES
    # =====================

    def prestar_libro(self, isbn: str, id_usuario: str) -> None:
        """
        Presta un libro a un usuario.
        
        Args:
            isbn: ISBN del libro a prestar
            id_usuario: ID del usuario que recibe el libro
            
        Raises:
            ValueError: Si el libro o usuario no existen, o el libro ya está prestado
        """
        isbn = (isbn or "").strip()
        id_usuario = (id_usuario or "").strip()

        if isbn not in self.__libros_disponibles:
            raise ValueError(f"No existe un libro con el ISBN '{isbn}'.")

        if id_usuario not in self.__usuarios:
            raise ValueError(f"No existe un usuario con el ID '{id_usuario}'.")

        libro = self.__libros_disponibles[isbn]
        usuario = self.__usuarios[id_usuario]

        # Verificar si el usuario ya tiene el libro
        if usuario.tiene_libro(isbn):
            raise ValueError(f"{usuario.nombre} ya tiene prestado este libro.")

        # Agregar el libro a la lista del usuario
        usuario.agregar_libro(libro)

    def devolver_libro(self, isbn: str, id_usuario: str) -> None:
        """
        Devuelve un libro prestado por un usuario.
        
        Args:
            isbn: ISBN del libro a devolver
            id_usuario: ID del usuario que devuelve el libro
            
        Raises:
            ValueError: Si el libro o usuario no existen, o el usuario no tiene el libro
        """
        isbn = (isbn or "").strip()
        id_usuario = (id_usuario or "").strip()

        if isbn not in self.__libros_disponibles:
            raise ValueError(f"No existe un libro con el ISBN '{isbn}'.")

        if id_usuario not in self.__usuarios:
            raise ValueError(f"No existe un usuario con el ID '{id_usuario}'.")

        libro = self.__libros_disponibles[isbn]
        usuario = self.__usuarios[id_usuario]

        if not usuario.tiene_libro(isbn):
            raise ValueError(f"{usuario.nombre} no tiene prestado este libro.")

        # Remover el libro de la lista del usuario
        usuario.remover_libro(libro)

    def listar_libros_prestados(self, id_usuario: str) -> list[Libro]:
        """
        Lista todos los libros prestados a un usuario.
        
        Args:
            id_usuario: ID del usuario
            
        Returns:
            list: Lista de libros prestados al usuario
            
        Raises:
            ValueError: Si el usuario no existe
        """
        id_usuario = (id_usuario or "").strip()

        if id_usuario not in self.__usuarios:
            raise ValueError(f"No existe un usuario con el ID '{id_usuario}'.")

        return self.__usuarios[id_usuario].libros_prestados

    def esta_prestado(self, isbn: str) -> bool:
        """
        Verifica si un libro está actualmente prestado.
        
        Args:
            isbn: ISBN del libro a verificar
            
        Returns:
            bool: True si el libro está prestado a algún usuario
        """
        isbn = isbn.strip()
        return any(usuario.tiene_libro(isbn) for usuario in self.__usuarios.values())

    # =====================
    # ESTADISTICAS
    # =====================

    def contar_libros_prestados(self) -> int:
        """
        Retorna la cantidad total de libros prestados.
        
        Returns:
            int: Cantidad de libros prestados
        """
        total_libros = len(self.__libros_disponibles)
        total_usuarios = len(self.__usuarios)
        libros_prestados = sum(u.cantidad_libros_prestados() for u in self.__usuarios.values())

        return {
            "total_libros": total_libros,
            "total_usuarios": total_usuarios,
            "libros_prestados": libros_prestados,
            "libros_disponibles": total_libros - libros_prestados
        }


