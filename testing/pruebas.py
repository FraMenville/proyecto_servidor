"""Archivo para probar las funciones una por una y verificar si algún parámetro ha cambiado en la página web."""

import requests
from typing import Optional, List, Dict
from bs4 import BeautifulSoup

url = "http://lat.motorsport.com/f1/results/2025/gp-de-espana-653362"

def get_soup(url: str) -> Optional[BeautifulSoup]:
    """Obtiene el contenido HTML de la página y lo convierte en un objeto BeautifulSoup."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return None
    
    return BeautifulSoup(response.text, "html.parser")

def get_table(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Obtiene la tabla de resultados de la carrera."""

    # Verifica si la sopa fue creada correctamente
    if not soup:
        return None
    
    #baja hasta la tabla:
    table = soup.find("div", {"class": "ms-table-wrapper"})
    return table

def get_rows(table: BeautifulSoup) -> List[BeautifulSoup]:
    """Obtiene todas las filas de la tabla de resultados."""

    # Verifica si la tabla fue obtenida correctamente
    if not table:
        return []
    return table.find_all("tr", {"class": "ms-table_row"}) or []

def parse_row(row: BeautifulSoup) -> Dict[str, str]:
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
    url = url
    soup = get_soup(url)
    table = get_table(soup)
    rows = get_rows(table)
    return [self._parse_row(row) for row in rows if row.find('td')]

resultados = fetch_results(url)
for resultado in resultados:
    print(resultado)