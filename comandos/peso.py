import os
import sys
from git import Repo

def obtener_tamaño_repositorio(ruta_repositorio):
    total_tamaño = 0
    for directorio_raiz, directorios, archivos in os.walk(ruta_repositorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            total_tamaño += os.path.getsize(ruta_archivo)
    return total_tamaño

def main():
    if len(sys.argv) != 2:
        print("Uso: python git_repo_size.py <palabra_clave>")
        return

    palabra_clave = sys.argv[1]
    
    try:
        repo = Repo('.')
        ruta_repositorio = repo.working_dir
    except:
        print("Error: No estás dentro de un repositorio Git")
        return

    tamaño_repositorio = obtener_tamaño_repositorio(ruta_repositorio)
    print(f"Tamaño del repositorio: {tamaño_repositorio / (1024*1024)} MB")

if __name__ == "__main__":
    main()
    
#Este código buscará la palabra clave "peso" y utilizará la ruta del repositorio actual para calcular el tamaño del repositorio. Si no estás dentro de un repositorio Git cuando ejecutas el programa, mostrará un mensaje de error.




