from app.core import Scraper

url = "http://lat.motorsport.com/f1/results/2025/gp-de-espana-653362/?st=RACE"
scrap = Scraper()

resultados = scrap.get_race_results(url)
print(f"Resultados: {len(resultados)} pilotos")
for resultado in resultados:
    print(f"Piloto: {resultado["piloto"]} en posición: #{resultado["posicion"]}")