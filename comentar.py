from git import Repo, GitCommandError
import os

def hacer_commit_si_hay_staging(repo_path='.'):
    try:
        repo = Repo(repo_path)

        if repo.bare:
            print("❌ No se puede hacer commit en un repositorio bare.")
            return False

        # Verifica si hay cambios en el área de staging
        staged_files = repo.index.diff("HEAD")  # archivos staged vs HEAD

        if not staged_files:
            print("⚠️ No hay archivos en el área de staging. No se puede hacer commit.")
            return False

        # Pregunta al usuario por el mensaje de commit
        commit_msg = input("📝 Ingresa el mensaje del commit: ").strip()
        if not commit_msg:
            print("❌ El mensaje de commit no puede estar vacío.")
            return False

        # Realiza el commit
        repo.index.commit(commit_msg)
        print("✅ Commit realizado con éxito.")
        return True

    except GitCommandError as e:
        print(f"❌ Error ejecutando comando Git: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    return False


if __name__ == "__main__":
    hacer_commit_si_hay_staging()
