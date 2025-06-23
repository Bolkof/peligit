¡Perfecto! Te ayudo a crear un nuevo script peligit que:

Se puede colocar en ~/.local/bin/

Ejecuta tu script peligit.py

Respeta el directorio desde donde se llamó el comando (usa pwd)

Te permite usarlo como si fuera un comando del sistema



---

✅ Paso 1: Crea la carpeta si no existe

mkdir -p ~/.local/bin


---

✅ Paso 2: Crea el script peligit

nano ~/.local/bin/peligit

Pega dentro esto:

#!/data/data/com.termux/files/usr/bin/bash
# Script peligit: ejecuta peligit.py desde el directorio actual del usuario

# Ejecutar el script Python en el directorio actual
python3 /data/data/com.termux/files/home/peligit/peligit.py "$@"

🔁 Asegúrate de que la ruta /data/data/com.termux/files/home/peligit/peligit.py sea correcta.
Si el archivo está en otro lado, ajústalo.

Guarda con Ctrl + O, luego Enter, y sal con Ctrl + X.


---

✅ Paso 3: Dale permisos de ejecución

chmod +x ~/.local/bin/peligit


---

✅ Paso 4: Asegúrate de que ~/.local/bin esté en tu $PATH

Añade esto al final de tu ~/.bashrc o ~/.zshrc:

export PATH="$HOME/.local/bin:$PATH"

Y recarga:

source ~/.bashrc   # o ~/.zshrc si usas zsh


---

✅ Verifica que funciona:

which peligit
# Debería decir: /data/data/com.termux/files/home/.local/bin/peligit

peligit estado
# Y mostrará la salida desde tu directorio actual


---

¿Quieres que te genere el contenido del script peligit.py también con los cambios para que use os.getcwd() correctamente?

