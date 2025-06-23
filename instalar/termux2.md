

---

✅ Paso 1: Crea el script wrapper

Ejecuta esto en Termux:

mkdir -p ~/.local/bin
nano ~/.local/bin/peligit

Y pega dentro:

#!/data/data/com.termux/files/usr/bin/bash
# Ejecuta peligit.py desde el directorio actual

cd "$(pwd)"  # Garantiza que se ejecute desde el directorio donde estás
python3 /data/data/com.termux/files/home/peligit/peligit.py "$@"

> 📝 Asegúrate de que la ruta al script peligit.py sea correcta. Si no, ajústala.



Guarda con Ctrl + O, luego Enter, y sal con Ctrl + X.


---

✅ Paso 2: Dale permisos de ejecución

chmod +x ~/.local/bin/peligit


---

✅ Paso 3: Asegúrate de que el sistema lo pueda encontrar

Agrega esto a tu ~/.bashrc o ~/.zshrc si aún no está:

export PATH="$HOME/.local/bin:$PATH"

Luego recarga:

source ~/.bashrc   # o ~/.zshrc si usas zsh


---

✅ Paso 4: Asegúrate de que tu peligit.py use os.getcwd() correctamente

En tu peligit.py, asegúrate de que esta parte esté así:

import os

# Esto mostrará la ubicación real desde donde se ejecutó el comando
repo = os.getcwd()
if not repo.endswith('/'):
    repo += '/'


---

✅ Resultado final esperado:

~ $ pwd
/data/data/com.termux/files/home
~ $ peligit estado
/data/data/com.termux/files/home/
---- ESTADO DEL REPOSITORIO ----
...


---


