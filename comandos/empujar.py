from git import Repo

def push_repo(repo_path='.'):
    """
    Realiza un git push en el repositorio indicado.
    
    Parámetros:
        repo_path (str): Ruta al repositorio. Por defecto el directorio actual.
    """
    repo = Repo(repo_path)

    # Verifica si hay cambios sin confirmar
    if repo.is_dirty(untracked_files=True):
        print("⚠️  Hay cambios sin confirmar. Por favor, confírmalos antes de hacer push.")

    # Pregunta al usuario si desea continuar
    respuesta = input("¿Deseas continuar con el push? (s/n): ").strip().lower()

    if respuesta == 's':
        try:
            origin = repo.remotes.origin
            result = origin.push()
            print("✅ ¡Push realizado con éxito!")
        except Exception as e:
            error_msg = str(e)
            if 'Authentication failed' in error_msg or 'exit code(128)' in error_msg:
                print("❌ Error al hacer push: Falló la autenticación. Verifica tu usuario/contraseña o token.")
            else:
                print(f"❌ Error al hacer push: {error_msg}")
    else:
        print("❎ Push cancelado por el usuario.")


# =========================
# Uso de la función
# =========================
if __name__ == "__main__":
    push_repo('.')  # Puedes cambiar '.' por cualquier ruta de repositorio
