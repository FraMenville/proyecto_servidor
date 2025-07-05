import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_BOT_KEY: str = os.getenv("TELEGRAM_BOT_KEY")
        self.LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
        self.URL_BASE: str = os.getenv("API_URL", "http://lat.motorsport.com/f1/results/2025/gp-de-espana-653362/?st=RACE")
        self.APP_NAME: str = os.getenv("APP_NAME", "RayoMcQueen")
        self.AUTHOR_NAME: str = os.getenv("AUTHOR_NAME", "Freddy")

    @classmethod
    def get_url_base(self) -> str:
        """Devuelve la url para el scraper."""
        return self.URL_BASE

    @classmethod
    def get_telegram_bot_key(self) -> str:
        """Devuelve la key del bot de Telegram."""
        return self.TELEGRAM_BOT_KEY
    
    @classmethod
    def get_app_name(self) -> str:
        """Devuelve el nombre de la aplicación."""
        return self.APP_NAME
    
    @classmethod
    def get_author_name(self) -> str:
        """Devuelve el nombre del autor de la aplicación."""
        return self.AUTHOR_NAME