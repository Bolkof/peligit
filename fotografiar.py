import git
from mnemonic import Mnemonic

def fotografiar(repo_path='.'):
    """
    Pide un mensaje, realiza un commit, obtiene el hash completo y genera una frase semilla BIP39 del hash.
    
    Args:
        repo_path (str): Ruta al repositorio Git (por defecto el directorio actual)
    """
    try:
        # Abrir el repositorio
        repo = git.Repo(repo_path)
        
        # Pedir el mensaje del commit
        mensaje = input("¿Cuál es el mensaje del commit? ")
        
        # Realizar el commit (asumiendo que los cambios ya están staged)
        commit = repo.index.commit(mensaje)
        
        # Obtener el hash completo
        hash_completo = commit.hexsha
        print(f"\nCommit realizado. Hash completo: {hash_completo}")
        
        # Convertir el hash hexadecimal a bytes
        hash_bytes = bytes.fromhex(hash_completo)
        
        # Crear instancia de Mnemonic para español
        mnemo = Mnemonic("spanish")
        
        # Generar frase semilla BIP39 (necesita 16, 20, 24, 28 o 32 bytes)
        # Ajustamos el hash para que tenga un tamaño válido
        adjusted_hash = hash_bytes[:32]  # Tomamos máximo 32 bytes
        if len(adjusted_hash) < 16:
            adjusted_hash = adjusted_hash.ljust(16, b'\x00')  # Rellenamos si es muy corto
            
        frase_semilla = mnemo.to_mnemonic(adjusted_hash)
        
        print("\nFrase semilla BIP39 generada:")
        print(frase_semilla)
        
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    fotografiar()
