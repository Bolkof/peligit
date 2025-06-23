import os
from comandos.polaroid import fotografiar as fotografiar
from comandos.estado import mostrar_estado

# Obtiene la ruta desde donde se llamó el comando
repo = os.environ.get('PWD', os.getcwd())
if not repo.endswith('/'):
    repo += '/'

def opciones(args):
    """
    Procesa los argumentos recibidos según las condiciones especificadas.
    """
    if not args:
        print("¡Hola! Soy Polaroid, tu asistente de Git.")
    elif len(args) == 1 and args[0] == "fotografiar":
        msn = None
        fotografiar(msn)
    elif len(args) == 2 and args[0] == "fotografiar":
        msn = args[1]
        fotografiar(msn)
    elif len(args) == 1 and args[0] == "estado":
        mostrar_estado()
    else:
        print("Comando no reconocido. Opciones válidas:")
        print("- fotografiar [mensaje]")
        print("- estado")

# Ejemplo de uso si se ejecuta directamente
if __name__ == "__main__":
    print(repo)  # Esto imprimirá la ruta desde donde se llamó el comando
    import sys
    opciones(sys.argv[1:])
    print(opciones)