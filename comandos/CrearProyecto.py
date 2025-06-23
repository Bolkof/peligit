import os
import re
from git import Repo

def inicializar_repositorio(ubicacion="", nombre=""):
    """
    Inicializa un repositorio Git.

    Args:
        ubicacion (str): La ruta donde se creará el repositorio.
                         Si está vacía, se usa el directorio de trabajo actual.
        nombre (str): El nombre de la carpeta para el repositorio.
                      Si no está vacía, se crea una subcarpeta con este nombre.
    """
    ruta_final_repositorio = ""

    # Determinar la ubicación base
    if not ubicacion:
        ruta_base = os.getcwd()
    else:
        ruta_base = ubicacion

    # Validar el nombre de la carpeta si se proporciona
    if nombre:
        # Regex para nombres de carpeta: alfanuméricos, espacios, guiones, guiones bajos
        if not re.fullmatch(r"^[a-zA-Z0-9\s\-_]+$", nombre):
            print(f"Error: El nombre de la carpeta '{nombre}' contiene caracteres no válidos.")
            return

        ruta_final_repositorio = os.path.join(ruta_base, nombre)
    else:
        ruta_final_repositorio = ruta_base

    # Crea el directorio si no existe
    if not os.path.exists(ruta_final_repositorio):
        try:
            os.makedirs(ruta_final_repositorio)
            print(f"Directorio '{ruta_final_repositorio}' creado.")
        except OSError as e:
            print(f"Error al crear el directorio '{ruta_final_repositorio}': {e}")
            return

    # Inicializa un nuevo repositorio
    try:
        repo = Repo.init(ruta_final_repositorio)
        print(f"Repositorio en '{ruta_final_repositorio}' inicializado.")
    except Exception as e:
        print(f"Error al inicializar el repositorio en '{ruta_final_repositorio}': {e}")
        return

    # Crea una nueva rama llamada 'primordial' si no existe
    if 'primordial' not in repo.heads:
        repo.create_head('primordial')
        print("Rama 'primordial' creada.")

    # Mueve la rama actual a 'primordial'
    if repo.head.ref != repo.heads.primordial:
        repo.heads.primordial.checkout()
        print("Rama 'primordial' activada.")
    else:
        print("La rama 'primordial' ya está activa.")

    print(f"Repositorio configurado exitosamente en '{ruta_final_repositorio}'.")

if __name__ == "__main__":
    # Ejemplos de uso:

#    print("\n--- Caso 1: Crear en el directorio actual sin nombre de carpeta ---")
#    inicializar_repositorio()

#    print("\n--- Caso 2: Crear en una ubicación específica sin nombre de carpeta ---")
#    # Asegúrate de que este directorio exista o sea writable
#    inicializar_repositorio(ubicacion="./mi_proyecto_base")

#    print("\n--- Caso 3: Crear en el directorio actual con nombre de carpeta ---")
#    inicializar_repositorio(nombre="mi_nuevo_repo")

#    print("\n--- Caso 4: Crear en una ubicación específica con nombre de carpeta ---")
#    inicializar_repositorio(ubicacion="./proyectos", nombre="repo_en_proyectos")

#    print("\n--- Caso 5: Nombre de carpeta inválido ---")
#    weé(nombre="mi/repo<invalido>")

#    print("\n--- Caso 6: Ubicación que no existe y no es el directorio actual con nombre de carpeta ---")
#    # Ten en cuenta que 'ubicacion_no_existente' debe ser un path válido para que os.makedirs funcione
#    # Si quieres que cree la ruta completa, os.makedirs lo hará por defecto.
#    inicializar_repositorio(ubicacion="./carpeta_nueva/otra_mas", nombre="repo_anidado")