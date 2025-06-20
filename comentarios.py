# modificar el imput no en el mensaje sino 3n su logica s8 rewive un string no vacio cerrar el orogramas



from git import Repo
import os
import platform

def mostrar_log_interactivo(repo_path='.'):
    try:
        repo = Repo(repo_path)

        if repo.bare:
            print("❌ Repositorio bare. No se puede mostrar el log.")
            return

        commits = list(repo.iter_commits('HEAD'))

        if not commits:
            print("⚠️ No hay commits en este repositorio.")
            return

        print("📜 Historial de commits (presiona Enter para continuar, o escribe 'salir' para salir):\n")

        for idx, commit in enumerate(commits):
            print(f"🔸  Commit {idx+1}:")
            print(f"Hash: {commit.hexsha[:7]}")
            print(f"Autor: {commit.author.name} <{commit.author.email}>")
            print(f"Fecha: {commit.committed_datetime}")
            print(f"Mensaje: {commit.message.strip()}")
            print("-")
 #           clear_console()

            user_input = input(">>>> Enter para continuar, 'salir' para salir: ").strip().lower()
            if user_input == "salir":
                print("👋 Saliendo del historial.")
                break

    except Exception as e:
        print(f"❌ Error: {e}")



#def clear_console():
#    """Clears the console screen."""
#    if platform.system() == "Windows":
#        os.system('cls')
#    else:
#        # For Linux/macOS
#        os.system('clear')

# This is your "manual-like" input (still using built-in input for simplicity)
#user_response = input("➡️ Enter para continuar, 'salir' para salir: ").strip().lower()

# After the user presses Enter, clear the console
#clear_console()

#if user_response == 'salir':
#    print("Saliendo del programa.")
#else:
#    print("¡Continuando con el programa!")
#    # Any other output will now appear on a fresh screen

if __name__ == "__main__":
    mostrar_log_interactivo()
