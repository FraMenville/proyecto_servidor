"""Scraper para obtener resultados de carreras de Fórmula 1 desde la página oficial de F1."""

import requests
from bs4 import BeautifulSoup
from typing import Optional, List, Dict

class Scraper:
    def __init__(self) -> None:
        pass

    def _get_soup(self) -> Optional[BeautifulSoup]:
        """Obtiene el contenido HTML de la página y lo convierte en un objeto BeautifulSoup."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error al obtener la página: {e}")
            return None
        
        return BeautifulSoup(response.text, "html.parser")

    def _get_table(self) -> Optional[BeautifulSoup]:
        """Obtiene la tabla de resultados de la carrera."""

        # Verifica si la sopa fue creada correctamente
        if not self.soup:
            return None
        
        #baja hasta la tabla:
        table = self.soup.find("div", {"class": "ms-table-wrapper"})
        return table
        
    def _get_rows(self) -> List[BeautifulSoup]:
        """Obtiene todas las filas de la tabla de resultados."""

        # Verifica si la tabla fue obtenida correctamente
        if not self.table:
            return []
        return self.table.find_all("tr", {"class": "ms-table_row"}) or []
        
    def _parse_row(self, row: BeautifulSoup) -> Dict[str, str]:
        """Parsea una fila de resultados y devuelve un diccionario con los datos."""
        
        # Verifica si la fila tiene datos, si no los tiene, devuelve un diccionario vacío
        if not row:
            return {"no data": "No hay datos disponibles"}
        
        data = {
            'posicion': row.find('td', {'class': 'ms-table_field--pos'}).get_text(strip=True),
            'numero': row.find('td', {'class': 'ms-table_field--number'}).get_text(strip=True),
            'piloto': row.find('span', {'class': 'name-short'}).get_text(strip=True) if row.find('span', {'class': 'name-short'}) else None,
            'equipo': row.find('span', {'class': 'team'}).get_text(strip=True),
            'vueltas': row.find('td', {'class': 'ms-table_field--laps'}).get_text(strip=True),
            'tiempo': row.find('td', {'class': 'ms-table_field--time'}).get_text(' ', strip=True),
            'intervalo': row.find('td', {'class': 'ms-table_field--interval'}).get_text(strip=True),
            'velocidad_promedio': row.find('td', {'class': 'ms-table_field--avg_speed'}).get_text(strip=True),
            'paradas': row.find('td', {'class': 'ms-table_field--pits'}).get_text(strip=True),
            'retiro': row.find('td', {'class': 'ms-table_field--retirement'}).get_text(strip=True) if row.find('td', {'class': 'ms-table_field--retirement'}) else None,
            'motor': row.find('td', {'class': 'ms-table_field--engine_make'}).get_text(strip=True)
        } 

        return data

    def fetch_results(self, url: str) -> List[dict]:
        self.url = url
        self.soup = self._get_soup()
        self.table = self._get_table()
        rows = self._get_rows()
        return [self._parse_row(row) for row in rows if row.find('td')]

    def get_race_results(self, url: str) -> list:
        self.url = url
        self.soup = self._get_soup()
        self.table = self._get_table()
        rows = self._get_rows()
        results = []
        
        for row in rows:
            if not row.find('td'):
                print("Fila sin datos, continuando...")
                continue
            results.append(self._parse_row(row))
        return results