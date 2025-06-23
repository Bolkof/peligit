import os
from git import Repo, GitCommandError

def obtener_rama_actual(repo):
    try:
        return f"Rama actual: {repo.active_branch.name}"
    except TypeError:
        return "No estás en una rama (detached HEAD)."

def estado_con_remoto(repo):
    try:
        rama = repo.active_branch
        tracking = rama.tracking_branch()
        if not tracking:
            return "Esta rama no está rastreando ninguna rama remota."

        ahead = sum(1 for _ in repo.iter_commits(f'{tracking}..{rama}'))
        behind = sum(1 for _ in repo.iter_commits(f'{rama}..{tracking}'))

        return f"La rama está {ahead} commits adelante y {behind} atrás de la remota."
    except GitCommandError:
        return "No se pudo obtener el estado con respecto a la remota."

def cambios_por_confirmar(repo):
    staged = [item.a_path for item in repo.index.diff("HEAD")]
    if staged:
        return "Cambios preparados para confirmación:\n" + "\n".join(f"  - {archivo}" for archivo in staged)
    return "No hay cambios preparados para confirmación."

def cambios_no_preparados(repo):
    unstaged = [item.a_path for item in repo.index.diff(None)]
    if unstaged:
        return "Cambios no preparados para confirmación:\n" + "\n".join(f"  - {archivo}" for archivo in unstaged)
    return "No hay cambios no preparados para confirmación."

def archivos_sin_seguimiento(repo):
    untracked = repo.untracked_files
    if untracked:
        return "Archivos sin seguimiento:\n" + "\n".join(f"  - {archivo}" for archivo in untracked)
    return "No hay archivos sin seguimiento."

def archivos_en_conflicto(repo):
    conflictos = [item.a_path for item in repo.index.unmerged_blobs().values()]
    if conflictos:
        return f"⚠️ Hay archivos en conflicto:\n" + "\n".join(f"  - {archivo}" for archivo in conflictos)
    return "✅ No hay archivos en conflicto."

def mostrar_estado():
    ruta = os.getcwd()
    try:
        repo = Repo(ruta)
        if repo.bare:
            print("El repositorio está vacío.")
            return

        print("---- ESTADO DEL REPOSITORIO ----")
        print(obtener_rama_actual(repo))
        print(estado_con_remoto(repo))
        print(cambios_por_confirmar(repo))
        print(cambios_no_preparados(repo))
        print(archivos_sin_seguimiento(repo))
        print(archivos_en_conflicto(repo))

    except Exception as e:
        print(f"No se pudo acceder al repositorio en {ruta}: {e}")

if __name__ == "__main__":
    mostrar_estado()
