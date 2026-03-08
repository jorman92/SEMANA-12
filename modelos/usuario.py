"""
Módulo Usuario - Entidad modelo para representar un usuario del sistema.

Este módulo define la clase Usuario que representa a un usuario registrado
en la biblioteca. Utiliza una lista para almacenar los libros prestados,
permitiendo modificaciones dinámicas según los préstamos y devoluciones.

Decisiones de diseño:
- Los libros prestados se almacenan en una lista porque es una colección
  dinámica que cambia frecuentemente (préstamos y devoluciones).
- La lista permite agregar y eliminar elementos eficientemente.
- Se usa encapsulamiento para proteger los datos del usuario.
"""
class Usuario:
    """
    Entidad Usuario (modelo).
    
    Representa a un usuario registrado en la biblioteca digital.
    Los libros prestados se almacenan en una lista para permitir
    modificaciones dinámicas.
    
    Attributes:
        __id_usuario (str): ID único del usuario
        __nombre (str): Nombre del usuario
        __libros_prestados (list): Lista de libros actualmente prestados
    """
    def __init__(self, id_usuario: str, nombre: str):
        """
        Inicializa un nuevo usuario.
        
        Args:
            id_usuario: ID único del usuario
            nombre: Nombre del usuario
        """
        self.__id_usuario = id_usuario.strip()
        self.__nombre = nombre.strip()
        self.__libros_prestados = []  # Lista para almacenar libros prestados

    @property
    def id_usuario(self) -> str:
        """Devuelve el ID del usuario."""
        return self.__id_usuario
    
    @property
    def nombre(self) -> str:
        """Devuelve el nombre del usuario."""
        return self.__nombre
    
    @property
    def libros_prestados(self) -> list:
        """Devuelve la lista de libros actualmente prestados."""
        return self.__libros_prestados.copy()  # Devuelve una copia para proteger la lista original
    
    def agregar_libro(self, libro) -> None:
        """
        Agrega un libro a la lista de préstamos.
        
        Args:
            libro: Objeto Libro a agregar
        """
        self.__libros_prestados.append(libro)

    def remover_libro(self, libro) -> bool:
        """
        Remueve un libro de la lista de préstamos.
        
        Args:
            libro: Objeto Libro a remover
            
        Returns:
            bool: True si se removió el libro, False si no estaba en la lista
        """
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)
            return True
        return False

    def tiene_libro(self, isbn: str) -> bool:
        """
        Verifica si el usuario tiene prestado un libro específico.
        
        Args:
            isbn: ISBN del libro a verificar
            
        Returns:
            bool: True si el usuario tiene el libro
        """
        return any(libro.isbn == isbn for libro in self.__libros_prestados)

    def cantidad_libros_prestados(self) -> int:
        """
        Retorna la cantidad de libros prestados.
        
        Returns:
            int: Número de libros prestados
        """
        return len(self.__libros_prestados)

    def __repr__(self) -> str:
        """Representación en string del usuario."""
        return f"Usuario(ID={self.id_usuario}, nombre={self.nombre})"

    def __eq__(self, other) -> bool:
        """
        Compara dos usuarios por su ID.
        
        Args:
            other: Otro objeto Usuario a comparar
            
        Returns:
            bool: True si los IDs son iguales
        """
        if not isinstance(other, Usuario):
            return False
        return self.__id_usuario == other.__id_usuario

    def __hash__(self) -> int:
        """Hash basado en el ID para usar en conjuntos."""
        return hash(self.__id_usuario)
