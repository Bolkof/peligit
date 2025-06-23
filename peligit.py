import argparse
import inspect

# Importaciones de comandos (descomentar y asegurar que existan los archivos)
#from comandos.add import add
#from comandos.bip39 import consultar_bip39, translate_lenguage
#from comandos.cambiarRama import cambiarRama
#from comandos.commit import git_commit_and_print
#from comandos.ignorados import mostar_archivos_ignorados
#from comandos.ignorar import agregar_a_gitignorare as ignolar
from peso import main as pesar
#from comandos.rasteados import rasteados
#from comandos.reset import reset
#from comandos.rm import rm
#from comandos.seguimiento import seguimiento
#from comandos.status import git_status as estado
from comandos.verRamas import verRamas
from comandos.verificarExistencia import verificarExistencia
from comandos.ls import ls # Corregido 'iimport'

# Variables globales o de configuración (inicializadas para que el código funcione)
boolRepo = False # Se asume que verificarExistencia() la actualizará.

# Funciones dummy para simular las que no están importadas o definidas
# Deberías reemplazarlas con tus implementaciones reales.
def consultar_bip39():
    print("Función consultar_bip39 no implementada.")

def translate_lenguage():
    print("Función translate_lenguage no implementada.")

def cambiarRama():
    print("Función cambiarRama no implementada.")

def git_commit_and_print():
    print("Función git_commit_and_print no implementada.")

def mostar_archivos_ignorados():
    print("Función mostar_archivos_ignorados no implementada.")

def ignolar():
    print("Función ignolar no implementada. ¿Imprime preguntas?")

def pesar():
    print("Función pesar no implementada.")

def rasteados():
    print("Función rasteados no implementada.")

def reset():
    print("Función reset no implementada.")

def rm():
    print("Función rm no implementada.")

def seguimiento():
    print("Función seguimiento no implementada.")

def estado():
    print("Función estado no implementada.")

def git_mv(arg1, arg2):
    print(f"Función git_mv no implementada. Recibió: {arg1}, {arg2}")

def git_clean_escoger():
    print("Función git_clean_escoger no implementada.")

def git_clean_selecionados():
    print("Función git_clean_selecionados no implementada.")

def git_cleanore_escoger():
    print("Función git_cleanore_escoger no implementada.")

def git_cleanore_selecionados():
    print("Función git_cleanore_selecionados no implementada.")

def agregar_todo():
    print("Función agregar_todo no implementada.")

def crear_bip39():
    print("Función crear_bip39 no implementada.")

def commit_comando(comando):
    # Esta función simula la determinación del comando de commit
    # Ajusta su lógica según tus necesidades reales.
    return f"comando_{comando}"

def boleano_a_preparacio():
    # Esta función simula la verificación de elementos en el escenario
    # Retorna True si hay algo para commitear, False en caso contrario.
    print("Verificando si hay elementos en la zona de preparación...")
    return True # Placeholder, reemplaza con tu lógica real

def commitiar(mensaje, comando):
    # Esta función simula la acción de commitear
    print(f"Realizando commit con mensaje: '{mensaje}' y comando: '{comando}'")
    # git_commit_and_print(mensaje) # Si esta es la función real a usar

def debug_print(*args, **kwargs):
    """
    Imprime un mensaje precedido por el número de línea desde donde fue llamada.
    Útil para depuración.
    """
    caller_frame = inspect.currentframe().f_back
    line_number = caller_frame.f_lineno
    print(f"linea {line_number}    ", end="")
    print(*args, **kwargs)

def opciones(argumentos):
    global boolRepo # Declarar que vamos a modificar la variable global boolRepo
    boolRepo = verificarExistencia() # Actualizar el estado del repositorio

    if not argumentos: # Manejar el caso de argumentos vacíos
        print("""Programa de línea de comandos, \nes un fork de git llamado Peligit""")
        return

    # peso
    if argumentos[0] == 'peso':
        if len(argumentos) == 1:
            debug_print("colocar la funcion que consulta el peso del repositorio:")
            pesar() # Llamada a la función pesar
        else:
            print('¡peso no recibe más argumentos!')

    # estado
    elif argumentos[0] == 'estado':
        if len(argumentos) == 1:
            estado() # Llamada a la función estado
            debug_print('Se ejecutó la función estado().')
        else:
            print('¡estado no recibe más argumentos!')

    # ignorados
    elif argumentos[0] == 'ignorados' and boolRepo:
        if len(argumentos) == 1:
            debug_print('para ignorados, se ejecuta la función mostar_archivos_ignorados().')
            mostar_archivos_ignorados()
        else:
            print('¡ignorados no recibe más parámetros!')

    # ignolar
    elif argumentos[0] == "ignolar" and boolRepo:
        if len(argumentos) == 1:
            ls()
            debug_print('No estoy seguro, pero la función ignolar imprime unas preguntas.')
            ignolar() # Llamada a la función ignolar
        else:
            print('¡ignolar no recibe más parámetros!')

    # agregar
    elif argumentos[0] == 'agregar' and boolRepo: # Corregido 'bollRepo' a 'boolRepo'
        debug_print('Llega hasta agregar la comparación de string')
        if len(argumentos) == 1:
            ls()
            add() # Asumiendo que 'add()' sin argumentos pide interacción
            debug_print('Se ejecutó la función add() para agregar archivos de forma interactiva.')
        else:
            debug_print("Aquí debe haber una función que elimine el primer elemento de la lista")
            # argumentos.pop(0) # Ya lo estamos manejando con 'argumentos[1:]' si add() acepta una lista
            # Si add() espera los archivos como argumentos, podrías pasar el resto de la lista:
            # add(*argumentos[1:])
            print("El comando 'agregar' con argumentos no está completamente implementado. ")
            print("Se espera que la función 'add' reciba los archivos directamente.")


    # fotografiar / commit
    elif argumentos[0] in ('fotografiar', 'grabar', 'filmar') and boolRepo: # Corregida la lógica del 'or'
        comando = commit_comando(argumentos[0])
        preparado = boleano_a_preparacio()
        if preparado:
            if len(argumentos) == 1:
                comentario = 'mensaje predefinido'
                commitiar(comentario, comando)
            elif len(argumentos) == 2:
                comentario = argumentos[1]
                commitiar(comentario, comando)
            else:
                print(f'El comando {argumentos[0]}, solo recibe un argumento que es el mensaje. Revise si el mensaje se encuentra entre comillas dobles o simples.')
        else:
            print(f'No tienes cosas dentro del escenario para ser {comando}.')

    # git mv o renombrar
    elif argumentos[0] == 'renombrar':
        if len(argumentos) == 3:
            git_mv(argumentos[1], argumentos[2])
            debug_print(f'Se ejecutó git_mv con los argumentos: {argumentos[1]}, {argumentos[2]}')
        else:
            print('Este comando espera dos argumentos:\n el primero, el archivo que se quiere renombrar;\n el segundo, el nombre que se quiere dar.\n\n Ambos argumentos también deben indicar la ubicación.')

    # limpiar
    elif argumentos[0] == 'limpiar':
        if len(argumentos) == 1:
            git_clean_escoger()
        elif len(argumentos) > 1:
            git_clean_selecionados()

    # limpiar ignorados
    elif argumentos[0] == 'limpiar-ignorados':
        if len(argumentos) == 1:
            git_cleanore_escoger()
        elif len(argumentos) > 1:
            git_cleanore_selecionados()

    # fotografiar-todo
    elif argumentos[0] == 'fotografiar-todo':
        # Definir 'comando' en este bloque si es necesario, ya que su alcance era local al bloque anterior.
        comando = 'fotografiar-todo' # Asignar el comando apropiado para esta acción.
        if len(argumentos) == 1:
            agregar_todo() # Agrega todos los archivos a la zona de preparación
            debug_print("Se agregaron todos los archivos a la zona de preparación.")
            comentario = 'mensaje predefinido'
            commitiar(comentario, comando)
        elif len(argumentos) == 2:
            comentario = argumentos[1]
            commitiar(comentario, comando)
        else:
            print(f'El comando {argumentos[0]}, solo recibe un argumento adicional que es el mensaje. Revise si el mensaje se encuentra entre comillas dobles o simples.')

    # bip 39
    elif argumentos[0] == 'bip39':
        if len(argumentos) == 1:
            consultar_bip39() # Llamada a la función que consulta el estado de bip39
            debug_print('Se consultó el estado de bip39.')
        elif len(argumentos) == 2:
            debug_print(f'Colocar argumentos = {argumentos[1]} como parámetro que reciba la función crear_bip39')
            # Si crear_bip39 espera el idioma como argumento:
            # crear_bip39(argumentos[1])
            crear_bip39() # Llamada a la función crear_bip39 (sin el argumento directamente aquí)
            debug_print(f'Se intentó crear BIP39 con idioma: {argumentos[1]}')
        else:
            print('El comando bip39 solo acepta un argumento opcional que es el idioma para crear una nueva clave.')

    else:
        print("""Programa de línea de comandos, \nes un fork de git llamado Peligit""")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convierte los argumentos en strings.")
    parser.add_argument('argumentos', nargs='*', help='Lista de argumentos')
    args = parser.parse_args()
    return args.argumentos

if __name__ == "__main__":
    # La siguiente línea está comentada para facilitar pruebas directas con 'argumentos'
    # Si quieres usar los argumentos de la línea de comandos, descoméntala.
    # argumentos = parse_arguments()

    # Argumentos de prueba (puedes cambiar esta lista para probar diferentes comandos)
    argumentos = ['bip39', 'es'] # Ejemplo: ['agregar', 'archivo.txt'], ['fotografiar', 'mi primer commit']

    print("Lista de argumentos recibidos:", argumentos)
    opciones(argumentos)
