from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError
import os

# Obtiene la ruta del repositorio local (directorio actual)
repo_path = os.getcwd()

try:
    # Abre el repositorio
    repo = Repo(repo_path)

    # Asegúrate de que el repositorio no sea un repositorio "bare"
    if not repo.bare:
        # Intenta obtener las últimas actualizaciones del origen remoto
        origin = repo.remotes.origin
        print("Intentando obtener los últimos cambios (pull)...")
        try:
            origin.pull()
            print("Pull completado con éxito.")
        except GitCommandError as e:
            print(f"Error durante el pull: {e}")
            print("Por favor, asegúrate de que tus cambios locales estén commiteados o guardados con 'stash'.")
    else:
        print(f"La ruta '{repo_path}' es un repositorio Git bare. No se pueden realizar operaciones que requieren un árbol de trabajo.")

except InvalidGitRepositoryError:
    print(f"Error: La ruta '{repo_path}' no es un repositorio Git válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
