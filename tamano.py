import git
import os

def peso(repo_path):
    # Abre el repositorio
    repo = git.Repo(repo_path)

    # Calcula el peso total
    total_size = 0
    for blob in repo.tree().traverse():
        total_size += blob.size

    # Convierte el tamaño a megabytes
    total_size_mb = total_size / (1024 * 1024)

    return total_size_mb