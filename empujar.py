from git import Repo
import sys

# Ruta al repositorio actual
repo_path = '.'
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
