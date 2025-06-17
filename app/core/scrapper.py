import requests
from bs4 import BeautifulSoup
from app.applog import get_logger

logger = get_logger("Scraper")
class ItemPrice:
    """Clase para representar un producto con su precio."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: {self.price if self.price is not None else 'No disponible'}"
    
class Scraper:
    """Clase para realizar scraping de precios de alimentos desde Numbeo."""
    
    BASE_URL = "https://www.numbeo.com/food-prices/country_result.jsp"

    def __init__(self, country: str, currency: str = "USD"):
        self.country = country
        self.currency = currency
        self.url = f"{self.BASE_URL}?country={self.country}&displayCurrency={self.currency}"

    def fetch_data(self):
        """Obtiene el HTML de la página y maneja errores de conexión."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            logger.info(f"Datos obtenidos correctamente para {self.country}")
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al obtener datos: {e}")
            return None

    def parse_data(self, html_content):
        """Extrae los precios de los alimentos desde el HTML."""
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", class_="data_wide_table new_bar_table")

        if not table:
            print("⚠ No se encontró la tabla de precios")
            return []

        rows = table.find_all("tr")[1:]  # Excluir encabezado
        item_prices = []

        for row in rows:
            columns = row.find_all("td")
            item_name = columns[0].text.strip()
            price_text = columns[1].find("span", class_="first_currency")  # Extraer solo el <span>

            if price_text:
                price = self.clean_price(price_text.text)
            else:
                price = None  # Si el precio no está presente

            item_prices.append(ItemPrice(item_name, price))  # Guardar datos en objetos

        return item_prices

    def clean_price(self, price_text):
        """Limpia el precio eliminando símbolos y convierte a número."""
        price_text = price_text.replace("$", "").replace(",", "").strip()
        try:
            return float(price_text)
        except ValueError:
            return None

    def get_item_prices(self):
        """Método principal para obtener los datos procesados."""
        html_content = self.fetch_data()
        return self.parse_data(html_content)