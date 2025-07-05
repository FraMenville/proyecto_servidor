# app/bot/commands/start.py
from telegram import Update
from telegram.ext import ContextTypes
from app.settings import Config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensaje = (
        f"👋 Bienvenido a {Config.get_app_name()}!\n\n"
        "Usa /ayuda para ver todos los comandos disponibles."
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mensaje,
        parse_mode="HTML"
    )
