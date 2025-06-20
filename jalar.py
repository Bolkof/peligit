# Importa la función desde el archivo error-pull.py
from error_pull import configurar_git_pull # Importa la función específica
from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError
import os
import subprocess

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
            # Aquí agregamos el parámetro -v para que sea más explícito el mensaje de error de GitPython
            # y coincida con el stderr que mencionaste
            origin.pull(rebase=False, no_rebase=False) # Intentamos un pull sin rebase/no-rebase explícito primero
            print("Pull completado con éxito.")
        except GitCommandError as e:
            # Captura el error específico de ramas divergentes
            if "fatal: Need to specify how to reconcile divergent branches." in e.stderr:
                print("\n¡ATENCIÓN! Se detectaron ramas divergentes.")
                print("Git necesita saber cómo quieres combinar los cambios.")
                # Llama a la función para configurar la estrategia de pull
                configuracion_exitosa = configurar_git_pull()
                if configuracion_exitosa:
                    print("\nPor favor, intenta el 'git pull' de nuevo después de configurar la estrategia.")
                else:
                    print("\nNo se pudo configurar la estrategia de pull. Por favor, revisa los errores anteriores.")
            else:
                # Otros errores durante el pull
                print(f"Error durante el pull: {e}")
                print("Por favor, asegúrate de que tus cambios locales estén commiteados o guardados con 'stash'.")
    else:
        print(f"La ruta '{repo_path}' es un repositorio Git bare. No se pueden realizar operaciones que requieren un árbol de trabajo.")

except InvalidGitRepositoryError:
    print(f"Error: La ruta '{repo_path}' no es un repositorio Git válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# --- Funciones relacionadas con los commits (mantener si las necesitas) ---
def get_commit_range():
    # Obtiene los dos últimos commits (nuevo y anterior)
    result = subprocess.run(["git", "rev-list", "--max-count=2", "HEAD"], capture_output=True, text=True)
    commits = result.stdout.strip().split('\n')
    if len(commits) < 2:
        return None, None
    return commits[1], commits[0]  # viejo, nuevo

def get_changed_files(old_commit, new_commit):
    # Lista archivos cambiados entre los dos commits
    result = subprocess.run(["git", "diff", "--name-only", old_commit, new_commit], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def main_commit_info(): # Renombrada para evitar conflicto con `main` si ya existe
    old_commit, new_commit = get_commit_range()
    if not old_commit or not new_commit:
        print("No se pudo determinar el rango de commits.")
        return

    print(f"{old_commit[:7]} >>> {new_commit[:7]}")  # Mostrar hash corto

    changed_files = get_changed_files(old_commit, new_commit)
    if changed_files:
        print("Archivos cambiados:")
        for f in changed_files:
            print(f" - {f}")
    else:
        print("No hubo archivos modificados.")

if __name__ == "__main__":
    # Puedes llamar a main_commit_info() si quieres que se ejecute también
    main_commit_info()
    pass # El código principal de pull se ejecuta directamente al inicio del script
