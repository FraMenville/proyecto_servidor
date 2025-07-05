# app/bot/commands/resultados.py
from telegram import Update
from telegram.ext import ContextTypes
from app.core import Scraper
from app.settings import Config
from app.applog import get_logger

logger = get_logger(f"{Config.get_app_name}: Command Module")

async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = Config.get_url_base()
    scraper = Scraper()
    data = scraper.get_race_results(url)

    if not data:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚠️ No se pudieron obtener los resultados."
        )
        logger.error(f"Error al entregar los resultados")
        return

    lines = ["🏁 Resultados de la carrera:\n"]
    for row in data:
        if row and row.get("posicion"):
            lines.append(
                f"*{row['posicion']}*. _{row['piloto']}_ ({row['equipo']}) – "
                f"*Vueltas: {row['vueltas']}* – Tiempo: {row['tiempo']}"
            )

    mensaje = "\n".join(lines)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mensaje,
        parse_mode="Markdown"
    )
