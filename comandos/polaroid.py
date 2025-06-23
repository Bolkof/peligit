import git
from git.exc import InvalidGitRepositoryError
from mnemonic import Mnemonic

# Variable global para la ruta del repositorio
try:
    repo = git.Repo('.')  # Por defecto usa el directorio actual
except InvalidGitRepositoryError:
    repo = None  # Si no es un repo Git válido

def fotografiar(mensaje=None):
    """
    Realiza un commit, obtiene el hash y genera una frase semilla BIP39.
    Si no se proporciona mensaje, lo pide por input.
    """
    if repo is None:
        print("❌ Usted no se encuentra dentro de un repositorio de Git.")
        return

    try:
        # Pedir mensaje si no se proporcionó
        if mensaje is None:
            mensaje = input("¿Cuál es el mensaje del commit? ")

        # Realizar el commit
        commit = repo.index.commit(mensaje)

        # Obtener hash
        hash_completo = commit.hexsha
        print(f"\n✅ Commit realizado. Hash completo: {hash_completo}")

        # Convertir hash a bytes
        hash_bytes = bytes.fromhex(hash_completo)

        # Generar frase semilla (ajustando a 16-32 bytes)
        mnemo = Mnemonic("spanish")
        adjusted_hash = hash_bytes[:32] or b'\x00' * 16  # Mínimo 16 bytes
        frase = mnemo.to_mnemonic(adjusted_hash)

        print("\n🔑 Frase semilla BIP39:")
        print(frase)

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    fotografiar()