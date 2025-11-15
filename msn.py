#!/usr/bin/env python3
import telebot
import sys
import os
from datetime import datetime

# ===== CONFIGURACIÓN =====
TOKEN = "AQUI_TU_TOKEN"
USER_ID = 123456789     # ID del usuario para envío de archivo

bot = telebot.TeleBot(TOKEN)

# Directorio actual del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ==========================
# MODO: ENVÍO DE ARCHIVO
# ==========================
def enviar_archivo(filepath):
    if not os.path.isfile(filepath):
        print(f"El archivo no existe: {filepath}")
        return

    with open(filepath, "rb") as f:
        bot.send_document(USER_ID, f)

    print(f"Archivo enviado a {USER_ID}: {filepath}")


# ==========================
# MODO: BOT ACTIVO
# ==========================

# Guardar textos
@bot.message_handler(content_types=['text'])
def guardar_texto(message):
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"trino_{fecha}.txt"
    fullpath = os.path.join(BASE_DIR, filename)

    with open(fullpath, "w", encoding="utf-8") as f:
        f.write(message.text)

    bot.reply_to(message, f"Mensaje guardado como {filename}")


# Guardar cualquier tipo de archivo con su nombre original
@bot.message_handler(content_types=[
    'document', 'photo', 'audio', 'video', 'voice', 'sticker', 'animation'
])
def guardar_archivo(message):
    file_info = None
    file_name = None

    # DOCUMENTOS (ya traen nombre)
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        file_name = message.document.file_name

    # FOTOS (NO traen nombre → generamos uno)
    elif message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = f"photo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

    # AUDIOS (si no trae nombre se asigna uno)
    elif message.audio:
        file_info = bot.get_file(message.audio.file_id)
        file_name = message.audio.file_name or f"audio_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.ogg"

    # NOTAS DE VOZ
    elif message.voice:
        file_info = bot.get_file(message.voice.file_id)
        file_name = f"voice_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.ogg"

    # VIDEOS
    elif message.video:
        file_info = bot.get_file(message.video.file_id)
        file_name = message.video.file_name or f"video_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"

    # GIFs / Animaciones
    elif message.animation:
        file_info = bot.get_file(message.animation.file_id)
        file_name = message.animation.file_name or f"anim_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"

    # Stickers
    elif message.sticker:
        file_info = bot.get_file(message.sticker.file_id)
        ext = ".webp" if message.sticker.is_animated is False else ".tgs"
        file_name = f"sticker_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}{ext}"

    # Guardado final
    if file_info and file_name:
        downloaded = bot.download_file(file_info.file_path)
        save_path = os.path.join(BASE_DIR, file_name)

        with open(save_path, "wb") as f:
            f.write(downloaded)

        bot.reply_to(message, f"Archivo guardado como {file_name}")


# ==========================
# CONTROL PRINCIPAL
# ==========================
if __name__ == "__main__":
    if len(sys.argv) == 2:
        enviar_archivo(sys.argv[1])
    else:
        print("Bot iniciado...")
        bot.infinity_polling()
