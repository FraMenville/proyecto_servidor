from telegram import Update
from telegram.ext import CallbackContext
from app.core import Scraper
from app.settings import Config

class BotController:
    def __init__(self):
        self.scraper = Scraper()

    def resultados_handler(self, update: Update, context: CallbackContext) -> None:
        chat_id = update.effective_chat.id
        url = Config.get_url_base()

        resultados = self.scraper.get_race_results(url)

        if not resultados:
            context.bot.send_message(chat_id=chat_id, text="No se pudieron obtener resultados 😓")
            return

        mensaje = self._formatear_resultados(resultados)
        context.bot.send_message(chat_id=chat_id, text=mensaje)

    def _formatear_resultados(self, data: list) -> str:
        lines = ["🏁 Resultados de la Carrera 🏁\n"]
        for piloto in data:
            if not piloto or "posicion" not in piloto:
                continue
            lines.append(f"{piloto['posicion']}. {piloto['piloto']} ({piloto['equipo']}) - Vueltas: {piloto['vueltas']} - Tiempo: {piloto['tiempo']}")
        return "\n".join(lines)
