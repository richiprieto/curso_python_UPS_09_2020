#!/usr/bin/env python
# -*- coding: utf-8 -*-
# direccion del bot solo prueba t.me/prueba_ups_bot
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1335347560:AAH2SemMjA6dSs9IxI0O6tFZ46LW-eKN9OU"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hola, este chatbot permite controlar su hogar")


def focosala_command(update, context):
    update.message.reply_text("Encendiendo el Foco de la Sala")
    print("Encendiendo foco de la sala")


def puertagarage_command(update, context):
    update.message.reply_text("Abriendo puerta del garage")
    print("Abriendo puerta del Garage")


def echo(update, context):
    # Podemos manejar cualquier texto que deseemos desde aqui
    update.message.reply_text(update.message.text)
    print("El texto que se recibio fue:", update.message.text)


def main():
    """Start the bot."""
    # Creamos el updater para conectarnos con la API de telegram
    updater = Updater(
        "1335347560:AAH2SemMjA6dSs9IxI0O6tFZ46LW-eKN9OU", use_context=True
    )

    # con dispatcher controlamos los manejadores
    dp = updater.dispatcher

    # aqui colocamos los comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("focosala", focosala_command))
    dp.add_handler(CommandHandler("puertagarage", puertagarage_command))

    # aqui haremos el manejo de cualquier texto
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Iniciamos el bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
