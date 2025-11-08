import os
from git import Repo
from git.exc import InvalidGitRepositoryError


# funcion creada para el comando 'peligit incorporar' sin mas argumentos


def interactive_git_add():
    """
    Función interactiva que muestra los archivos modificados y permite
    seleccionar cuáles agregar al staging area mediante números.
    """
    try:
        # Obtener el repositorio actual
        repo = Repo(os.getcwd())
        
        # Verificar que no estemos en un estado de merge o conflicto
        if repo.is_dirty(untracked_files=True):
            print("📁 Repositorio Git encontrado")
        else:
            print("❌ No hay cambios para agregar")
            return
            
    except InvalidGitRepositoryError:
        print("❌ No se encontró un repositorio Git en esta ubicación")
        return
    
    # Obtener archivos modificados, eliminados y sin track
    changed_files = []
    
    # Archivos modificados y sin track
    untracked_files = repo.untracked_files
    for file in untracked_files:
        changed_files.append(("untracked", file))
    
    # Archivos modificados
    for item in repo.index.diff(None):
        changed_files.append(("modified", item.a_path))
    
    # Archivos eliminados
    for item in repo.index.diff(None):
        if item.deleted_file:
            changed_files.append(("deleted", item.a_path))
    
    # Archivos en staging (solo para información)
    staged_files = [item.a_path for item in repo.index.diff("HEAD")]
    
    if not changed_files:
        print("✅ No hay archivos modificados para agregar")
        return
    
    # Mostrar archivos disponibles
    print("\n📋 Archivos modificados/sin track:")
    print("=" * 50)
    
    for i, (status, file_path) in enumerate(changed_files, 1):
        status_icon = {
            "modified": "🟡",
            "untracked": "🟢", 
            "deleted": "🔴"
        }.get(status, "⚪")
        
        print(f"{i:2d}. {status_icon} [{status:9}] {file_path}")
    
    # Mostrar archivos ya en staging
    if staged_files:
        print(f"\n📥 Archivos ya en staging area:")
        for file in staged_files:
            print(f"    📌 {file}")
    
    # Solicitar selección de archivos
    print("\n" + "=" * 50)
    print("Selecciona los archivos para agregar al staging:")
    print("• Ingresa números separados por comas (ej: 1,3,5)")
    print("• 'a' o 'all' para agregar todos")
    print("• 'q' o 'quit' para salir")
    
    while True:
        try:
            selection = input("\n👉 Tu selección: ").strip().lower()
            
            if selection in ['q', 'quit']:
                print("👋 Saliendo sin agregar archivos")
                return
            
            if selection in ['a', 'all']:
                # Agregar todos los archivos
                files_to_add = [file_path for _, file_path in changed_files]
                repo.index.add(files_to_add)
                print(f"✅ Agregados {len(files_to_add)} archivos al staging area")
                return
            
            # Procesar selección numérica
            selected_numbers = [num.strip() for num in selection.split(',')]
            files_to_add = []
            
            for num_str in selected_numbers:
                if not num_str:
                    continue
                    
                try:
                    num = int(num_str)
                    if 1 <= num <= len(changed_files):
                        status, file_path = changed_files[num - 1]
                        files_to_add.append(file_path)
                    else:
                        print(f"⚠️  Número {num} fuera de rango. Rango válido: 1-{len(changed_files)}")
                        
                except ValueError:
                    print(f"⚠️  '{num_str}' no es un número válido")
            
            if files_to_add:
                # Agregar archivos seleccionados
                repo.index.add(files_to_add)
                print(f"✅ Agregados {len(files_to_add)} archivos al staging area:")
                for file in files_to_add:
                    print(f"   📌 {file}")
                return
            else:
                print("❌ No se seleccionaron archivos válidos. Intenta nuevamente.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada por el usuario")
            return
        except Exception as e:
            print(f"❌ Error al agregar archivos: {e}")
            return

def git_add_specific_files(file_paths):
    """
    Función para agregar archivos específicos al staging area.
    
    Args:
        file_paths (list): Lista de rutas de archivos a agregar
    """
    try:
        repo = Repo(os.getcwd())
        repo.index.add(file_paths)
        print(f"✅ Archivos agregados al staging area: {file_paths}")
        return True
    except Exception as e:
        print(f"❌ Error al agregar archivos: {e}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    print("🚀 Selector Interactivo de Git Add")
    print("=" * 40)
    
    # Usar la función interactiva
    interactive_git_add()
    
    # Ejemplo de uso programático
    # git_add_specific_files(["archivo1.txt", "archivo2.py"])