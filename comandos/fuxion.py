import os
import sys
from git import Repo, GitCommandError
from git.exc import InvalidGitRepositoryError, GitError

# comando peligit2 fuxionar


def git_merge_robust(branch_name, merge_message=None, strategy=None, abort_on_conflict=True):
    """
    Función robusta para realizar git merge con manejo de errores y opciones avanzadas.
    
    Args:
        branch_name (str): Nombre de la rama a mergear
        merge_message (str, optional): Mensaje para el commit de merge. Por defecto None
        strategy (str, optional): Estrategia de merge. Opciones: 'ort', 'recursive', 'octopus', 'ours'
        abort_on_conflict (bool): Si es True, aborta el merge en caso de conflicto. Por defecto True
    
    Returns:
        dict: Diccionario con el resultado y detalles del merge
    """
    
    result = {
        'success': False,
        'message': '',
        'conflicts': [],
        'merge_type': None,
        'commit_hash': None
    }
    
    try:
        # Validar parámetros
        if not branch_name or not isinstance(branch_name, str):
            result['message'] = "❌ El nombre de la rama debe ser un string válido"
            return result
        
        # Obtener el repositorio actual
        repo = Repo(os.getcwd())
        
        # Verificar que el repositorio esté limpio
        if repo.is_dirty():
            result['message'] = "❌ El repositorio tiene cambios sin commit. Por favor, commit o stash los cambios antes del merge."
            return result
        
        # Verificar que la rama objetivo existe
        if branch_name not in [ref.name for ref in repo.references]:
            # Intentar con formato completo
            full_branch_name = f"origin/{branch_name}"
            if full_branch_name not in [ref.name for ref in repo.references]:
                result['message'] = f"❌ La rama '{branch_name}' no existe"
                return result
            branch_name = full_branch_name
        
        # Obtener la rama actual
        current_branch = repo.active_branch.name
        result['current_branch'] = current_branch
        result['target_branch'] = branch_name
        
        print(f"🔄 Iniciando merge de '{branch_name}' en '{current_branch}'")
        
        # Verificar si es un fast-forward merge
        base = repo.merge_base(current_branch, branch_name)
        if not base:
            result['message'] = f"❌ No hay ancestro común entre {current_branch} y {branch_name}"
            return result
        
        # Determinar el tipo de merge
        if repo.commit(branch_name) in repo.commit(current_branch).parents:
            result['merge_type'] = 'already_merged'
            result['message'] = f"✅ La rama '{branch_name}' ya está mergeada en '{current_branch}'"
            result['success'] = True
            return result
        
        # Realizar el merge
        try:
            merge_result = repo.git.merge(
                branch_name,
                m=merge_message,
                no_ff=True,  # Siempre crear commit de merge
                strategy=strategy if strategy else 'ort'
            )
            
            result['success'] = True
            result['message'] = f"✅ Merge completado exitosamente"
            result['commit_hash'] = repo.head.commit.hexsha
            result['merge_type'] = 'merge_commit'
            
            print(f"✅ Merge completado: {merge_result}")
            
        except GitCommandError as e:
            error_msg = str(e)
            
            # Manejar conflictos
            if 'CONFLICT' in error_msg:
                result['merge_type'] = 'conflict'
                result['conflicts'] = _extract_conflicts(repo)
                
                print("⚠️  Se produjeron conflictos durante el merge:")
                for conflict in result['conflicts']:
                    print(f"   🔥 {conflict}")
                
                if abort_on_conflict:
                    print("🔄 Abortando merge debido a conflictos...")
                    repo.git.merge('--abort')
                    result['message'] = "❌ Merge abortado debido a conflictos. Resuelve los conflictos manualmente."
                else:
                    result['message'] = "⚠️  Merge con conflictos. Por favor, resuelve los conflictos manualmente y haz commit."
            
            else:
                result['message'] = f"❌ Error durante el merge: {error_msg}"
        
    except InvalidGitRepositoryError:
        result['message'] = "❌ No se encontró un repositorio Git válido"
    except GitError as e:
        result['message'] = f"❌ Error de Git: {e}"
    except Exception as e:
        result['message'] = f"❌ Error inesperado: {e}"
    
    return result

def _extract_conflicts(repo):
    """Extrae la lista de archivos en conflicto"""
    conflicts = []
    for item in repo.index.unmerged_blobs().values():
        for stage, blob in item:
            if stage != 0:  # Stage 0 significa sin conflicto
                conflicts.append(blob.path)
    return list(set(conflicts))  # Remover duplicados

def git_merge_interactive():
    """
    Función interactiva para realizar merge de forma guiada
    """
    try:
        repo = Repo(os.getcwd())
        
        # Obtener ramas disponibles (excluyendo la actual)
        current_branch = repo.active_branch.name
        branches = [ref.name for ref in repo.references if ref.name != current_branch and 'HEAD' not in ref.name]
        
        if not branches:
            print("❌ No hay otras ramas disponibles para mergear")
            return
        
        print(f"\n🌿 Rama actual: {current_b}")
        print("\n📋 Ramas disponibles:")
        for i, branch in enumerate(branches, 1):
            print(f"  {i}. {branch}")
        
        try:
            selection = input("\n👉 Selecciona el número de la rama a mergear: ").strip()
            selected_index = int(selection) - 1
            
            if 0 <= selected_index < len(branches):
                selected_branch = branches[selected_index]
                
                # Opciones de merge
                print(f"\n🔄 Mergeando '{selected_branch}' en '{current_branch}'")
                print("Opciones:")
                print("1. Merge normal (crear commit de merge)")
                print("2. Fast-forward (si es posible)")
                print("3. Merge con mensaje personalizado")
                
                option = input("👉 Selecciona opción (1-3, Enter para 1): ").strip() or "1"
                
                if option == "1":
                    result = git_merge_robust(selected_branch)
                elif option == "2":
                    result = _git_merge_fast_forward(selected_branch)
                elif option == "3":
                    message = input("📝 Mensaje para el commit de merge: ")
                    result = git_merge_robust(selected_branch, merge_message=message)
                else:
                    result = git_merge_robust(selected_branch)
                
                # Mostrar resultado
                _display_merge_result(result)
                
            else:
                print("❌ Selección inválida")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def _git_merge_fast_forward(branch_name):
    """Merge fast-forward específico"""
    try:
        repo = Repo(os.getcwd())
        repo.git.merge(branch_name, ff='only')
        return {
            'success': True,
            'message': f'✅ Fast-forward merge completado',
            'merge_type': 'fast_forward',
            'commit_hash': repo.head.commit.hexsha
        }
    except GitCommandError as e:
        return {
            'success': False,
            'message': f'❌ No se pudo hacer fast-forward: {e}'
        }

def _display_merge_result(result):
    """Muestra el resultado del merge de forma legible"""
    print(f"\n{'='*50}")
    if result['success']:
        print("✅ MERGE EXITOSO")
        print(f"Tipo: {result.get('merge_type', 'N/A')}")
        if result.get('commit_hash'):
            print(f"Commit: {result['commit_hash'][:8]}")
    else:
        print("❌ MERGE FALLIDO")
        print(f"Razón: {result['message']}")
        
        if result.get('conflicts'):
            print("\n📋 Archivos en conflicto:")
            for conflict in result['conflicts']:
                print(f"   🔥 {conflict}")
            print("\n💡 Para resolver conflictos:")
            print("   1. Edita los archivos marcados con conflictos")
            print("   2. git add <archivos_resueltos>")
            print("   3. git commit -m 'Resuelve conflictos de merge'")
    print(f"{'='*50}")

def git_merge_abort():
    """Aborta un merge en progreso"""
    try:
        repo = Repo(os.getcwd())
        repo.git.merge('--abort')
        print("✅ Merge abortado exitosamente")
        return True
    except GitCommandError:
        print("❌ No hay merge en progreso para abortar")
        return False

# Ejemplos de uso
if __name__ == "__main__":
    print("🔄 MERGE ROBUSTO CON GITPYTHON")
    print("=" * 40)
    
    # Uso programático
    # result = git_merge_robust("develop", merge_message="Merge feature importante")
    
    # Uso interactivo
    git_merge_interactive()
    
    # Para abortar merge
    # git_merge_abort()