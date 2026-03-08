"""
Sistema de Gestión de Biblioteca Digital
========================================

Punto de entrada principal del sistema.
Implementa un menú interactivo en consola para probar todas las
funcionalidades del sistema de biblioteca.

Arquitectura por capas:
- modelos/: Contiene las entidades (Libro, Usuario)
- servicios/: Contiene la lógica de negocio (BibliotecaServicio)
- main.py: Punto de entrada con interfaz de usuario en consola

Decisiones de diseño:
- El main.py solo contiene la interfaz de usuario, no lógica de negocio
- Todas las operaciones se delegan al servicio
- Se manejan excepciones para mostrar mensajes amigables al usuario
"""

from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 50)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL")
    print("=" * 50)
    print("\n--- GESTIÓN DE LIBROS ---")
    print("1.  Agregar libro")
    print("2.  Quitar libro")
    print("3.  Buscar libro por título")
    print("4.  Buscar libro por autor")
    print("5.  Buscar libro por categoría")
    print("6.  Listar todos los libros")
    print("\n--- GESTIÓN DE USUARIOS ---")
    print("7.  Registrar usuario")
    print("8.  Dar de baja usuario")
    print("9.  Listar usuarios")
    print("\n--- PRÉSTAMOS ---")
    print("10. Prestar libro")
    print("11. Devolver libro")
    print("12. Listar libros prestados a un usuario")
    print("\n--- ESTADÍSTICAS ---")
    print("13. Ver estadísticas del sistema")
    print("\n0.  Salir")
    print("-" * 50)


def pausar():
    """Pausa la ejecución esperando una tecla."""
    input("\nPresione Enter para continuar...")


def agregar_libro(servicio: BibliotecaServicio):
    """Función para agregar un nuevo libro."""
    print("\n--- AGREGAR LIBRO ---")
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    
    try:
        libro = servicio.agregar_libro(isbn, titulo, autor, categoria)
        print(f"\n✓ Libro agregado exitosamente: {libro}")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def quitar_libro(servicio: BibliotecaServicio):
    """Función para quitar un libro."""
    print("\n--- QUITAR LIBRO ---")
    isbn = input("ISBN del libro a eliminar: ")
    
    try:
        servicio.quitar_libro(isbn)
        print(f"\n✓ Libro con ISBN '{isbn}' eliminado exitosamente.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def buscar_por_titulo(servicio: BibliotecaServicio):
    """Función para buscar libros por título."""
    print("\n--- BUSCAR POR TÍTULO ---")
    titulo = input("Título a buscar: ")
    
    resultados = servicio.buscar_por_titulo(titulo)
    
    if resultados:
        print(f"\n✓ Se encontraron {len(resultados)} libro(s):")
        for libro in resultados:
            print(f"  - {libro.titulo} | {libro.autor} | ISBN: {libro.isbn} | Categoría: {libro.categoria}")
    else:
        print("\n✗ No se encontraron libros con ese título.")


def buscar_por_autor(servicio: BibliotecaServicio):
    """Función para buscar libros por autor."""
    print("\n--- BUSCAR POR AUTOR ---")
    autor = input("Autor a buscar: ")
    
    resultados = servicio.buscar_por_autor(autor)
    
    if resultados:
        print(f"\n✓ Se encontraron {len(resultados)} libro(s):")
        for libro in resultados:
            print(f"  - {libro.titulo} | {libro.autor} | ISBN: {libro.isbn} | Categoría: {libro.categoria}")
    else:
        print("\n✗ No se encontraron libros de ese autor.")


def buscar_por_categoria(servicio: BibliotecaServicio):
    """Función para buscar libros por categoría."""
    print("\n--- BUSCAR POR CATEGORÍA ---")
    categoria = input("Categoría a buscar: ")
    
    resultados = servicio.buscar_por_categoria(categoria)
    
    if resultados:
        print(f"\n✓ Se encontraron {len(resultados)} libro(s):")
        for libro in resultados:
            print(f"  - {libro.titulo} | {libro.autor} | ISBN: {libro.isbn} | Categoría: {libro.categoria}")
    else:
        print("\n✗ No se encontraron libros en esa categoría.")


def listar_libros(servicio: BibliotecaServicio):
    """Función para listar todos los libros."""
    print("\n--- CATÁLOGO DE LIBROS ---")
    
    libros = servicio.listar_libros()
    
    if libros:
        print(f"\nTotal de libros: {len(libros)}")
        for libro in libros:
            prestado = " (PRESTADO)" if servicio.esta_prestado(libro.isbn) else ""
            print(f"  - {libro.titulo} | {libro.autor} | ISBN: {libro.isbn} | Categoría: {libro.categoria}{prestado}")
    else:
        print("\n✗ No hay libros en el catálogo.")


def registrar_usuario(servicio: BibliotecaServicio):
    """Función para registrar un nuevo usuario."""
    print("\n--- REGISTRAR USUARIO ---")
    id_usuario = input("ID de usuario: ")
    nombre = input("Nombre: ")
    
    try:
        usuario = servicio.registrar_usuario(id_usuario, nombre)
        print(f"\n✓ Usuario registrado exitosamente: {usuario}")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def dar_baja_usuario(servicio: BibliotecaServicio):
    """Función para dar de baja un usuario."""
    print("\n--- DAR DE BAJA USUARIO ---")
    id_usuario = input("ID del usuario a dar de baja: ")
    
    try:
        servicio.dar_baja_usuario(id_usuario)
        print(f"\n✓ Usuario con ID '{id_usuario}' dado de baja exitosamente.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def listar_usuarios(servicio: BibliotecaServicio):
    """Función para listar todos los usuarios."""
    print("\n--- USUARIOS REGISTRADOS ---")
    
    usuarios = servicio.listar_usuarios()
    
    if usuarios:
        print(f"\nTotal de usuarios: {len(usuarios)}")
        for usuario in usuarios:
            libros = usuario.cantidad_libros_prestados()
            print(f"  - ID: {usuario.id_usuario} | Nombre: {usuario.nombre} | Libros prestados: {libros}")
    else:
        print("\n✗ No hay usuarios registrados.")


def prestar_libro(servicio: BibliotecaServicio):
    """Función para prestar un libro a un usuario."""
    print("\n--- PRESTAR LIBRO ---")
    isbn = input("ISBN del libro: ")
    id_usuario = input("ID del usuario: ")
    
    try:
        servicio.prestar_libro(isbn, id_usuario)
        libro = servicio.obtener_libro(isbn)
        usuario = servicio.obtener_usuario(id_usuario)
        print(f"\n✓ Libro '{libro.titulo}' prestado exitosamente a {usuario.nombre}.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def devolver_libro(servicio: BibliotecaServicio):
    """Función para devolver un libro."""
    print("\n--- DEVOLVER LIBRO ---")
    isbn = input("ISBN del libro: ")
    id_usuario = input("ID del usuario: ")
    
    try:
        servicio.devolver_libro(isbn, id_usuario)
        libro = servicio.obtener_libro(isbn)
        print(f"\n✓ Libro '{libro.titulo}' devuelto exitosamente.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def listar_libros_prestados(servicio: BibliotecaServicio):
    """Función para listar los libros prestados a un usuario."""
    print("\n--- LIBROS PRESTADOS ---")
    id_usuario = input("ID del usuario: ")
    
    try:
        libros = servicio.listar_libros_prestados(id_usuario)
        usuario = servicio.obtener_usuario(id_usuario)
        
        if libros:
            print(f"\n{usuario.nombre} tiene {len(libros)} libro(s) prestado(s):")
            for libro in libros:
                print(f"  - {libro.titulo} | {libro.autor} | ISBN: {libro.isbn}")
        else:
            print(f"\n{usuario.nombre} no tiene libros prestados.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def ver_estadisticas(servicio: BibliotecaServicio):
    """Función para ver estadísticas del sistema."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    
    stats = servicio.estadisticas()
    
    print(f"\n  Total de libros: {stats['total_libros']}")
    print(f"  Total de usuarios: {stats['total_usuarios']}")
    print(f"  Libros prestados: {stats['libros_prestados']}")
    print(f"  Libros disponibles: {stats['libros_disponibles']}")


def cargar_datos_prueba(servicio: BibliotecaServicio):
    """Carga datos de prueba para demostrar el sistema."""
    print("\n--- CARGANDO DATOS DE PRUEBA ---")
    
    # Agregar libros
    libros = [
        ("978-3-16-148410-0", "El Quijote", "Miguel de Cervantes", "Clásicos"),
        ("978-0-7432-7356-5", "El Código Da Vinci", "Dan Brown", "Misterio"),
        ("978-0-452-28423-4", "1984", "George Orwell", "Ciencia Ficción"),
        ("978-0-06-112008-4", "Matar a un ruiseñor", "Harper Lee", "Clásicos"),
        ("978-0-14-243724-7", "El Gran Gatsby", "F. Scott Fitzgerald", "Clásicos"),
        ("978-0-307-47427-8", "Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico"),
        ("978-0-679-76489-8", "Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía"),
    ]
    
    for isbn, titulo, autor, categoria in libros:
        try:
            servicio.agregar_libro(isbn, titulo, autor, categoria)
            print(f"  ✓ Agregado: {titulo}")
        except ValueError:
            pass  # Ignorar si ya existe
    
    # Registrar usuarios
    usuarios = [
        ("U001", "Juan Pérez"),
        ("U002", "María García"),
        ("U003", "Carlos López"),
    ]
    
    for id_usuario, nombre in usuarios:
        try:
            servicio.registrar_usuario(id_usuario, nombre)
            print(f"  ✓ Registrado: {nombre}")
        except ValueError:
            pass  # Ignorar si ya existe
    
    print("\n✓ Datos de prueba cargados exitosamente.")


def main():
    """
    Función principal del sistema.
    
    Inicializa el servicio de biblioteca y ejecuta el menú interactivo.
    """
    print("\n" + "=" * 50)
    print("  BIENVENIDO AL SISTEMA DE BIBLIOTECA DIGITAL")
    print("=" * 50)
    
    # Inicializar el servicio de biblioteca
    servicio = BibliotecaServicio()
    
    # Preguntar si cargar datos de prueba
    print("\n¿Desea cargar datos de prueba? (s/n): ", end="")
    if input().lower() == 's':
        cargar_datos_prueba(servicio)
        pausar()
    
    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            agregar_libro(servicio)
            pausar()
        elif opcion == "2":
            quitar_libro(servicio)
            pausar()
        elif opcion == "3":
            buscar_por_titulo(servicio)
            pausar()
        elif opcion == "4":
            buscar_por_autor(servicio)
            pausar()
        elif opcion == "5":
            buscar_por_categoria(servicio)
            pausar()
        elif opcion == "6":
            listar_libros(servicio)
            pausar()
        elif opcion == "7":
            registrar_usuario(servicio)
            pausar()
        elif opcion == "8":
            dar_baja_usuario(servicio)
            pausar()
        elif opcion == "9":
            listar_usuarios(servicio)
            pausar()
        elif opcion == "10":
            prestar_libro(servicio)
            pausar()
        elif opcion == "11":
            devolver_libro(servicio)
            pausar()
        elif opcion == "12":
            listar_libros_prestados(servicio)
            pausar()
        elif opcion == "13":
            ver_estadisticas(servicio)
            pausar()
        elif opcion == "0":
            print("\n¡Gracias por usar el Sistema de Biblioteca Digital!")
            print("Hasta pronto.\n")
            break
        else:
            print("\n✗ Opción no válida. Por favor, intente de nuevo.")
            pausar()


if __name__ == "__main__":
    main()
    