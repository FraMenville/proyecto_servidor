from app.core import Scrapper

scrap = Scrapper()

resultados = scrap.get_race_results()
for resultado in resultados:
    print(f"Piloto: {resultado["piloto"]} en posición: #{resultado["posicion"]}")