from git import Repo, InvalidGitRepositoryError

def ver_commits():
    """
    Permite al usuario ver los commits de un repositorio Git local.
    Pregunta cuántos commits desea ver (máximo 10) y muestra
    los 7 primeros caracteres del hash y la primera línea del comentario de cada commit.
    """
    try:
        # Intenta abrir el repositorio en el directorio actual
        repo = Repo('.')
    except InvalidGitRepositoryError:
        print("Error: No se encontró un repositorio Git en el directorio actual.")
        print("Asegúrate de ejecutar este script dentro de un repositorio Git.")
        return

    while True:
        try:
            num_commits_str = input("¿Cuántos commits quieres ver? (Máximo 10): ")
            num_commits = int(num_commits_str)
            if 1 <= num_commits <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    print(f"\nMostrando los últimos {num_commits} commits:")
    print("---")

    # Itera sobre los commits
    for i, commit in enumerate(repo.iter_commits('HEAD', max_count=num_commits)):
        print(f"Hash: {commit.hexsha[:7]}")
        # Obtiene solo la primera línea del mensaje del commit
        first_line_comment = commit.message.strip().split('\n')[0]
        print(f"Comentario: {first_line_comment}")
        print("---")

if __name__ == "__main__":
    ver_commits()
