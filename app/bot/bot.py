from telegram.ext import Application, CommandHandler

from app.settings import Config
from app.applog import get_logger
from app.bot.commands import start
from app.bot.registry import register_commands

logger = get_logger(f"[{Config.get_app_name()}: Bot Module]")

TOKEN = Config.get_telegram_bot_key()  

async def post_init(application: Application):
    """Función que se ejecuta después de que la aplicación se haya inicializado."""
    logger.info("🔗 Configurando el webhook del bot de Telegram...")
    await application.bot.delete_webhook(drop_pending_updates=True)

def main():
    """Función principal del bot"""

    logger.info("🔗 Iniciando el bot de Telegram...")
    
    # Verifica que el token esté 
    if not TOKEN:
        logger.error("❌ No se encontró TELEGRAM_BOT_KEY en las variables de entorno")
        raise ValueError("Token de Telegram no configurado")
    else:
        logger.info("✅ Token de Telegram encontrado")

    app = Application.builder()\
                .token(TOKEN)\
                .post_init(post_init)\
                .build()

    # Handlers
    register_commands(app)
    
    try:
        logger.info("Bot iniciado. Escuchando comandos...")
        app.run_polling()
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")
        raise e