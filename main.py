import requests
import gemini
import json
import rich
import os
import time
from dotenv import load_dotenv

load_dotenv(".env")

NEWSAPI = os.environ["NEWS_API"]

rich.print("[green]Cargando noticias de 3 sitios.")
news = json.loads(requests.get(f"{NEWSAPI}/getall/*").text)

rich.print("[green]Filtrando noticias")
res = gemini.filter_links(tuple(news))
resjson: list[str] = json.loads(res
                                .replace("```json", "")
                                .replace("```", "")
                    )["market_transfer_links"]

for url in resjson:
    site = None
    if "planetabj" in url:
        site = "planetabj"
    elif "tycsports" in url:
        site = "tycsports"
    elif "bolavip" in url:
        site = "bolavip"
    
    if site:
        time.sleep(10)
        page = url.split("/")[-2 if url.endswith("/") else -1]
        rich.print(f"[green]Cargando {site}")

        data = json.loads(requests.get(f"{NEWSAPI}/get/{site}/{page}").text)
        title, subtitle, content = (data["title"], data["subtitle"], data["content"])

        rich.print(f"[green]Analizando el articulo de {site}")
        transfer_data = json.loads(gemini.player_data(title, subtitle, content)
                                .replace("```json", "")
                                .replace("```", ""))
        
        print(f"BocaMarketMonitor AI cree que la transferencia de {transfer_data["player_name"]} desde {transfer_data["from"]} hacia {transfer_data["to"]} tiene un {transfer_data["possibilities"]}% de pasar.\nResumen del articulo: {transfer_data["summary"]}")
