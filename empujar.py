
import git
import os

def git_pull(repo_path, remote_name='origin', branch_name='main'):
    """
    Realiza un 'git pull' en un repositorio local.

    Args:
        repo_path (str): La ruta al directorio del repositorio local.
        remote_name (str, optional): El nombre del remoto del cual jalar (por defecto es 'origin').
        branch_name (str, optional): El nombre de la rama a jalar (por defecto es 'main').
    """
    try:
        # Abre el repositorio existente
        repo = git.Repo(repo_path)

        # Verifica si el remoto existe
        if remote_name not in [remote.name for remote in repo.remotes]:
            print(f"Error: El remoto '{remote_name}' no existe en el repositorio.")
            return

        # Obtiene el objeto del remoto
        origin = repo.remotes[remote_name]

        print(f"Realizando git pull en '{repo_path}' desde el remoto '{remote_name}' en la rama '{branch_name}'...")

        # Realiza el pull
        # El método pull() devuelve una lista de objetos que representan los cambios que se trajeron.
        # Puedes capturar esta salida si necesitas procesarla.
        pull_info = origin.pull(branch_name)

        # Imprime información sobre el pull
        for info in pull_info:
            print(f"  Referencia actualizada: {info.ref}")
            print(f"  Estado: {info.flags} (Ver `git.remote.FetchInfo` para más detalles)")
            if info.note:
                print(f"  Nota: {info.note}")
            if info.commit:
                print(f"  Último commit local después del pull: {info.commit.hexsha}")
            else:
                print("  No se detectó un nuevo commit específico para esta referencia.")

        print("¡Git pull completado exitosamente!")

    except git.InvalidGitRepositoryError:
        print(f"Error: '{repo_path}' no es un repositorio Git válido.")
    except Exception as e:
        print(f"Ocurrió un error al realizar el git pull: {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Define la ruta a tu repositorio local
    # ¡Asegúrate de cambiar esto a la ruta real de tu repositorio!
    # Por ejemplo, si tu repositorio está en 'C:\Users\TuUsuario\MiProyectoGit'
    # o '/home/tu_usuario/MiProyectoGit'
    local_repository_path = os.getcwd()

    # Asegúrate de que la ruta exista y sea un repositorio Git
    if not os.path.exists(local_repository_path):
        print(f"Error: La ruta '{local_repository_path}' no existe.")
    elif not os.path.isdir(os.path.join(local_repository_path, '.git')):
        print(f"Error: La ruta '{local_repository_path}' no parece ser un repositorio Git (no se encontró el directorio .git).")
    else:
        git_pull(local_repository_path)

        # Ejemplo de pull desde una rama específica (si no es 'main' o 'master')
        # git_pull(local_repository_path, branch_name='develop')
