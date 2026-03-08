"""
Módulo Libro - Entidad modelo para representar un libro en el sistema.

Este módulo define la clase Libro que representa un libro dentro del sistema
de biblioteca digital. Utiliza una tupla para almacenar título y autor,
aprovechando la inmutabilidad de las tuplas para datos que no cambian.

Decisiones de diseño:
- Título y autor se almacenan en una tupla porque son datos inmutables
  que no cambiarán durante la vida del objeto. Las tuplas son más eficientes
  en memoria y acceso que las listas para datos estáticos.
- Se usa encapsulamiento con atributos privados y properties para controlar
  el acceso a los datos.
- El ISBN es el identificador único del libro.
"""
class Libro:

    """
    Entidad Libro (modelo).
    
    Representa un libro dentro del sistema de biblioteca digital.
    El título y autor se almacenan como tupla (inmutable) para optimizar
    el rendimiento y garantizar que estos datos no cambien.
    
    Atributos:
        __isbn (str): ISBN del libro (identificador único)
        __titulo_autor (tuple): Tupla con (título, autor) - inmutable
        __categoria (str): Categoría del libro
    """

    def __init__(self, titulo: str, autor: str, isbn: str, categoria: str):
        """
        Inicializa un nuevo libro.
        
        Args:
            isbn: ISBN único del libro
            titulo: Título del libro
            autor: Autor del libro
            categoria: Categoría del libro
        """
        self.__isbn = isbn.strip()
        # Tupla para almacenar título y autor (inmutable)
        # Esto mejora el rendimiento ya que estos datos no cambian
        self.__titulo_autor = (titulo.strip(), autor.strip())
        self.__categoria = categoria.strip()

    @property
    def isbn(self) -> str:
        """Devuelve el ISBN del libro."""
        return self.__isbn
    
    @property
    def titulo(self) -> str:
        """Devuelve el título del libro."""
        return self.__titulo_autor[0]
    
    @property
    def autor(self) -> str:
        """Devuelve el autor del libro."""
        return self.__titulo_autor[1]
    
    @property
    def categoria(self) -> str:
        """Devuelve la categoría del libro."""
        return self.__categoria
    
    def __str__(self) -> str:
        """Devuelve una representación en cadena del libro."""
        return f"Libro(ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria})"
    
    def __eq__(self, other) -> bool:
        """Compara dos libros por su ISBN."""
        if isinstance(other, Libro):
            return self.isbn == other.isbn
        return False
    
    def __hash__(self) -> int:
        """Devuelve el hash del libro basado en su ISBN."""
        return hash(self.isbn)
    
