# app/bot/commands/status.py
from telegram import Update
from telegram.ext import ContextTypes

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    texto = "✅ Estoy en línea y listo para servirte."
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=texto
    )
