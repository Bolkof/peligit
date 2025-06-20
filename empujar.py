from git import Repo

# Ruta al repositorio actual
repo_path = '.'
repo = Repo(repo_path)

# Verifica si hay cambios sin confirmar
if repo.is_dirty(untracked_files=True):
    print("⚠️  Hay cambios sin confirmar. Por favor, confírmalos antes de hacer push.")
    # Pregunta al usuario si desea continuar
    respuesta = input(" o ¿Deseas continuar con el push? (s/n): ").strip().lower()
    if respuesta == 's':
        try:
            origin = repo.remotes.origin
            origin.push()
            print("✅ ¡Push realizado con éxito!")
        except Exception as e:
            print(f"❌ Error al hacer push: {e}")
    else:
        print("❎ Push cancelado por el usuario.")
