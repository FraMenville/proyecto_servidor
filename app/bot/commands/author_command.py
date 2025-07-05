# app/bot/commands/autor.py
from telegram import Update
from telegram.ext import ContextTypes
from app.settings import Config
from app.applog import get_logger

logger = get_logger(f"{Config.get_app_name}: Command Module")

async def autor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    autor = Config.get_author_name()
    texto = f"✍️ Este bot fue creado por {autor}."

    logger.info("Enviando información sobre el autor del bot")
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=texto
    )
