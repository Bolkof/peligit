import subprocess

def configurar_git_pull():
    """
    Pregunta al usuario qué estrategia de 'git pull' prefiere (merge, rebase, o ff-only)
    y configura esa preferencia para el repositorio local actual.
    """
    print("\n--- Configuración de Estrategia de 'git pull' ---")
    print("Cuando tus ramas local y remota difieren, ¿cómo quieres que Git las combine?")
    print("1. Merge (fusionar): Crea un nuevo commit de fusión. Mantiene el historial completo.")
    print("2. Rebase (reubicar): Re-aplica tus commits locales sobre los remotos. Historial más lineal.")
    print("3. Fast-forward Only (solo avance rápido): Solo permite la actualización si no hay conflictos.")

    while True:
        opcion = input("Elige una opción (1, 2 o 3): ")
        if opcion == '1':
            comando = "git config pull.rebase false"
            estrategia = "Merge"
            break
        elif opcion == '2':
            comando = "git config pull.rebase true"
            estrategia = "Rebase"
            break
        elif opcion == '3':
            comando = "git config pull.ff only"
            estrategia = "Fast-forward Only"
            break
        else:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")

    try:
        # Ejecuta el comando git en el shell
        # Usamos `shell=True` si el comando no se divide, pero `.split()` es más seguro.
        # Aquí, como ya lo estamos dividiendo, `shell=False` (por defecto) está bien.
        result = subprocess.run(comando.split(), check=True, capture_output=True, text=True)
        print(f"\n¡Perfecto! La estrategia '{estrategia}' ha sido configurada exitosamente para este repositorio.")
        print("Ahora, cuando ejecutes 'git pull', se usará esta preferencia.")
        return True # Indica que la configuración fue exitosa
    except subprocess.CalledProcessError as e:
        print(f"\nError al configurar Git: {e}")
        print(f"Salida de error: {e.stderr}")
        return False # Indica que la configuración falló
    except FileNotFoundError:
        print("\nError: El comando 'git' no se encontró. Asegúrate de que Git esté instalado y en tu PATH.")
        return False # Indica que la configuración falló

# Nota: No llames a la función directamente en error-pull.py.
# Se importará y se llamará desde tu script principal.
