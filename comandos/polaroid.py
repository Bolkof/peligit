import git
from mnemonic import Mnemonic
#import polaroid.fotografiar

# Variable global para la ruta del repositorio
repo = git.Repo('.')  # Por defecto usa el directorio actual

def fotografiar(mensaje):#=None):
    """
    Realiza un commit, obtiene el hash y genera una frase semilla BIP39.
    Si no se proporciona mensaje, lo pide por input.
    """
    try:
        global repo  # Usamos la variable global
        
        # Pedir mensaje si no se proporcionó
        if mensaje is None:
            mensaje = input("¿Cuál es el mensaje del commit? ")
        
        # Realizar el commit
        commit = repo.index.commit(mensaje)
        
        # Obtener hash
        hash_completo = commit.hexsha
        print(f"\nCommit realizado. Hash completo: {hash_completo}")
        
        # Convertir hash a bytes
        hash_bytes = bytes.fromhex(hash_completo)
        
        # Generar frase semilla (ajustando a 16-32 bytes)
        mnemo = Mnemonic("spanish")
        adjusted_hash = hash_bytes[:32] or b'\x00'*16  # Mínimo 16 bytes
        frase = mnemo.to_mnemonic(adjusted_hash)
        
        print("\nFrase semilla BIP39:")
        print(frase)
        
    except Exception as e:
        print(f"Error: {e}")

#def opciones(args):
#    """
#    Procesa los argumentos recibidos según las condiciones especificadas.
#    """
#    if not args:
#        print("¡Hola! Soy Polaroid, tu asistente de Git.")
#    elif len(args) == 1 and args[0] == "fotografiar":
#        fotografiar()
#    elif len(args) == 2 and args[0] == "fotografiar":
#        print('fotografiar con comentario')
#    elif len(args) == 1 and args[0] == "estado":
#        print("Estado del repositorio: OK")
#    else:
#        print("Comando no reconocido. Opciones válidas:")
#        print("- fotografiar [mensaje]")
#        print("- estado")

# Ejemplo de uso si se ejecuta directamente
if __name__ == "__main__":
#    import sys
#    opciones(sys.argv[1:])
     fotografiar()