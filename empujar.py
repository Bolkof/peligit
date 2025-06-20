from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError
import os

# Obtiene la ruta del repositorio local (directorio actual)
repo_path = os.getcwd()

try:
    # Abre el repositorio
    repo = Repo(repo_path)

    # Asegúrate de que el repositorio no sea un repositorio "bare"
    # Un repositorio bare no tiene un árbol de trabajo y se usa típicamente como servidor.
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

        # Obtiene los commits entre HEAD y el commit anterior (HEAD@{1})
        # Esto muestra los commits que acaban de llegar a tu rama actual.
        print("\n--- Commits Recientes ---")
        try:
            commits = repo.git.log("HEAD@{1}..HEAD", "--oneline")
            if commits:
                print(commits)
            else:
                print("No se encontraron nuevos commits entre HEAD@{1} y HEAD.")
        except GitCommandError as e:
            print(f"Error al obtener el historial de commits: {e}")

        # Obtiene las diferencias (diff) entre HEAD y el commit anterior
        print("\n--- Diferencias (HEAD@{1} vs HEAD) ---")
        try:
            diff = repo.git.diff("HEAD@{1}", "HEAD")
            if diff:
                print(diff)
            else:
                print("No se encontraron diferencias entre HEAD@{1} y HEAD.")
        except GitCommandError as e:
            print(f"Error al obtener las diferencias: {e}")

    else:
        print(f"La ruta '{repo_path}' es un repositorio Git bare. No se pueden realizar operaciones que requieren un árbol de trabajo.")

except InvalidGitRepositoryError:
    print(f"Error: La ruta '{repo_path}' no es un repositorio Git válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
