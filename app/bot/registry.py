from telegram.ext import CommandHandler, Application
from app.bot.commands import (
    start,
    ayuda,
    autor,
    status,
    resultados
)

# Lista de tuplas (nombre_comando, función_manejadora)
COMMANDS = [
    ("start", start),
    ("ayuda", ayuda),
    ("autor", autor),
    ("status", status),
    ("resultados", resultados)
]

def register_commands(application: Application) -> None:
    """Agrega todos los CommandHandler al objeto Application."""
    for cmd, handler in COMMANDS:
        application.add_handler(CommandHandler(cmd, handler))
