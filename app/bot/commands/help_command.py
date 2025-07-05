# app/bot/commands/ayuda.py
from telegram import Update
from telegram.ext import ContextTypes
from app.settings import Config
from app.applog import get_logger

logger = get_logger(f"{Config.get_app_name}: Command Module")

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    comandos = [
        "/start : Inicio del bot",
        "/ayuda : Muestra esta ayuda",
        "/autor : Información del autor",
        "/status : Estado del bot",
        "/resultados : Resultados de la carrera"
    ]
    texto = "📖 Lista de comandos:\n" + "\n".join(comandos)

    logger.info("Enviando mensaje de ayuda")
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=texto,
        parse_mode="MarkdownV2"
    )
