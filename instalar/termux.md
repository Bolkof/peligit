


# ✅ Paso a Paso: Ejecutar un Programa Peligit Globalmente en Termux (sin mover archivos)




---

1. 🔧 Instalar Dependencias Básicas

pkg update && pkg upgrade
pkg install python git -y


---

2. ⬇️ Clonar el Repositorio (si viene de GitHub)

git clone https://github.com/Bolkof/peligit.git && peligit

(Si ya tienes la carpeta peligit, navega directamente a ella)



---

3. 📥 Instalar Dependencias

pip install -r requirements.txt


---

4. 🚀 Crear un Script Lanzador Global

1. Abre el editor de texto para crear el lanzador:

vim $PREFIX/bin/peligit


5. Pega este contenido (ajustado a tu caso):

#!/data/data/com.termux/files/usr/bin/bash
cd /data/data/com.termux/files/home/peligit/
python peligit.py "$@"



6. Dar permisos de ejecución al script:

chmod +x $PREFIX/bin/peligit




---

✅ Ahora puedes ejecutar tu programa globalmente:

Desde cualquier carpeta:

$ peligit

También puedes pasarle argumentos:

$ peligit comentar
