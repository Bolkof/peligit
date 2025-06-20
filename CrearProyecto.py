import os
from git import Repo

def inicializar_repositorio(nombre_repositorio):
    # Si nombre_repositorio es "[aqui]" o está vacío, usa el directorio actual
    if not nombre_repositorio or nombre_repositorio.lower() == "[aqui]":
        nombre_repositorio = os.getcwd()

    # Crea el directorio si no existe
    if not os.path.exists(nombre_repositorio):
        os.makedirs(nombre_repositorio)

    # Inicializa un nuevo repositorio
    repo = Repo.init(nombre_repositorio)

    # Crea una nueva rama llamada 'primordial'
    repo.create_head('primordial')

    # Mueve la rama actual a 'primordial'
    repo.heads.primordial.checkout()

    print(f"Repositorio en '{nombre_repositorio}' creado y rama 'primordial' creada y activa.")

if __name__ == "__main__":
    # Puedes ejecutar esta parte directamente para probar la función
    nombre_repo = input("Ingrese el nombre del repositorio (presiona Enter para usar el directorio actual o '[aqui]'): ")
    inicializar_repositorio(nombre_repo)
