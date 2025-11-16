import os
from comandos.polaroid import fotografiar as fotografiar
from comandos.estado import mostrar_estado
from comandos.add1 import interactive_git_add
from comandos.jalar import main_commit_info 
from comandos.empujar import push_repo
#from comandos.fuxion import git_merge_interactive()





# Obtiene la ruta desde donde se llamó el comando
repo = os.environ.get('PWD', os.getcwd())
if not repo.endswith('/'):
    repo += '/'
    

def argumento_404():
    # 1️⃣ Obtener la ruta absoluta del archivo actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # 2️⃣ Definir la carpeta "comandos" relativa a donde está este script
    carpeta = os.path.join(ruta_actual, "comandos")

    # 3️⃣ Verificar si la carpeta existe
    if not os.path.exists(carpeta):
        print(f"❌ No se encontró la carpeta: {carpeta}")
        return

    # 4️⃣ Escanear la carpeta y obtener todos los archivos .py
    archivos_py = [
        archivo for archivo in os.listdir(carpeta)
        if archivo.endswith(".py")
    ]

    # 5️⃣ Leer el archivo ignorar.txt dentro de la carpeta "comandos"
    ruta_ignorar = os.path.join(carpeta, "ignorar.txt")

    if not os.path.exists(ruta_ignorar):
        print(f"⚠️ No se encontró el archivo ignorar.txt en {carpeta}")
        ignorar = []
    else:
        with open(ruta_ignorar, "r", encoding="utf-8") as f:
            ignorar = [linea.strip() for linea in f if linea.strip()]

    # 6️⃣ Crear una tercera lista con elementos que NO aparecen en ambas listas
    resultado = list(set(archivos_py) ^ set(ignorar))
    
# Eliminar ".py" del final si lo tienen
    imprimir = [nombre[:-3] if nombre.endswith(".py") else nombre for nombre in resultado]

# 7️⃣ Imprimir la tercera lista en vertical
  #  print("Archivos únicos en una de las listas:\n")
    for item in imprimir:
        print(f'- {item}')



# 🧩 Llamada a la función
#if __name__ == "__main__":
#    argumento_404()


def opciones(args):
    """
    Procesa los argumentos recibidos según las condiciones especificadas.
    """
    if not args:
        print("¡Hola! Soy Polaroid, tu asistente de Git.")
        argumento_404()
    elif len(args) == 1 and args[0] == "fotografiar":
        msn = None
        fotografiar(msn)
    elif len(args) == 2 and args[0] == "fotografiar":
        msn = args[1]
        fotografiar(msn)
    elif len(args) == 1 and args[0] == "estado":
        mostrar_estado()
    elif len(args) == 1 and args[0] == "empujar":
        push_repo()
    elif len(args) == 1 and args[0] == "jalar":
        main_commit_info()
    elif len(args) == 1 and args[0] == "incorporar":
        interactive_git_add()
    else:
        print("Comando no reconocido. Opciones válidas:")
        argumento_404()
   #     print("- fotografiar [mensaje]")
   #     print("- estado")

# Ejemplo de uso si se ejecuta directamente
if __name__ == "__main__":
    print(repo)  # Esto imprimirá la ruta desde donde se llamó el comando
    import sys
    opciones(sys.argv[1:])
    print(opciones)
    
    
  
