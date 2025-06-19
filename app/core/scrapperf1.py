import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self) -> None:
        self.soup = self._get_soup()
        self.table = self.get_table()
        self.row = self.get_row()
        self.parse = self.parse_row()
        pass

    def _get_soup(self) -> BeautifulSoup:
        url = "http://lat.motorsport.com/f1/results/2025/gp-de-espana-653362/?st=RACE"

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error al obtener la página: {e}")
            return None
        
        return BeautifulSoup(response.text, "html.parser")

    def get_table(self) -> BeautifulSoup:
        #baja hasta la tabla:
        table = self.soup.find("div", {"class": "ms-table_wrapper"})
        return table
        
    def get_row(self) -> BeautifulSoup:
        #extrae todas las filas
        row = self.table.find_all("tr", {"class": "ms-table_row"})
        if row:
            return row
        
    def parse_row(self) -> dict:
        #extrae los datos de la tabla
        data = {
            'posicion': self.row.find('td', {'class': 'ms-table_field--pos'}).get_text(strip=True),
            'numero': self.row.find('td', {'class': 'ms-table_field--number'}).get_text(strip=True),
            'piloto': self.row.find('span', {'class': 'name-short'}).get_text(strip=True) if self.row.find('span', {'class': 'name-short'}) else None,
            'equipo': self.row.find('span', {'class': 'team'}).get_text(strip=True),
            'vueltas': self.row.find('td', {'class': 'ms-table_field--laps'}).get_text(strip=True),
            'tiempo': self.row.find('td', {'class': 'ms-table_field--time'}).get_text(' ', strip=True),
            'intervalo':self.row.find('td', {'class': 'ms-table_field--interval'}).get_text(strip=True),
            'velocidad_promedio': self.row.find('td', {'class': 'ms-table_field--avg_speed'}).get_text(strip=True),
            'paradas': self.row.find('td', {'class': 'ms-table_field--pits'}).get_text(strip=True),
            'retiro': self.row.find('td', {'class': 'ms-table_field--retirement'}).get_text(strip=True) if self.row.find('td', {'class': 'ms-table_field--retirement'}) else None,
            'motor': self.row.find('td', {'class': 'ms-table_field--engine_make'}).get_text(strip=True)
        } 

        return data

    def get_race_results(self) -> list:
        rows = self.row
        results = []
        
        for row in rows:
            if not row.find('td'):
                continue
            results.append(self.parse_row(row))
        return results


"""
    if __name__ == "__main__":
        soup = get_soup()
        if soup:
            resultados = get_race_results(soup)
            for resultado in resultados:
                print(f"Piloto: {resultado["piloto"]} en posición: #{resultado["posicion"]}")"""