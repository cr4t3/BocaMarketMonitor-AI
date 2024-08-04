import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Función para obtener URLs de noticias de Planeta Boca Juniors
def get_planetabj_news_urls():
    url = 'https://planetabj.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar todos los enlaces que contienen '/boca-juniors' en el href
    news_links = soup.find_all('a', href=True)
    news_urls = set(urljoin('https://planetabj.com', link['href']) for link in news_links if '/boca-juniors' in link['href'])
    
    return list(news_urls)

# Función para obtener URLs de noticias de BolaVIP
"""<a 
    href="https://bolavip.com/ar/boca/sin-la-presencia-de-marcos-rojo-ni-de-pol-fernandez-diego-martinez-hara-cambios-en-la-formacion-de-boca" 
    target="_self" 
    class="card-title__link link-factory-custom-style">
    Diego Martínez hará cambios en la formación de Boca
   </a>"""

def get_bolavip_news_urls():
    url = 'https://bolavip.com/ar/resultados/futbol/equipo/boca/6861eac1-6a03-4954-aee7-6a2694fc86a2/noticias'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar todos los enlaces que contienen '/boca-juniors' en el href
    news_links = soup.find_all('a', href=True)
    news_urls = set(urljoin('https://bolavip.com/ar/boca', link['href']) for link in news_links if '/ar/boca' in link['href'])
    
    return list(news_urls)

# Función para obtener URLs de noticias de TyC Sports
def get_tycsports_news_urls():
    url = 'https://www.tycsports.com/boca-juniors'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar todos los enlaces que contienen '/boca-juniors' en el href
    news_links = soup.find_all('a', href=True)
    news_urls = set(urljoin('https://www.tycsports.com', link['href']) for link in news_links if '/boca-juniors' in link['href'])
    
    return list(news_urls)

def get_all_news_urls():
    sites = [get_planetabj_news_urls, get_tycsports_news_urls, get_bolavip_news_urls]
    news = []
    for site in sites:
        news.extend(site())
    return news

def load_planetabj_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find("h1", class_="article-title")
        title = title_tag.get_text(strip=True)

        subtitle_tag = soup.find("p", class_="article-excerpt")
        subtitle = subtitle_tag.get_text(strip=True)

        content_tag = soup.find("div", class_="article-body")
        content = content_tag.get_text(strip=True)

        return title, subtitle, content
    except requests.RequestException as e:
        print(f"Error al cargar la página de Planeta Boca Juniors: {e}")
        return None

def load_bolavip_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find("h1", class_="article-title")
        title = title_tag.get_text(strip=True)

        subtitle_tag = soup.find("p", class_="article-excerpt")
        subtitle = subtitle_tag.get_text(strip=True)

        content_tag = soup.find("div", class_="article-body")
        content = content_tag.get_text(strip=True)

        return title, subtitle, content
    except requests.RequestException as e:
        print(f"Error al cargar la página de Planeta Boca Juniors: {e}")
        return None

def load_tycsports_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True)

        subtitle_tag = soup.find("p", class_="description")
        subtitle = subtitle_tag.get_text(strip=True)

        content_tag = soup.find_all("p", class_="")
        content = "\n".join([tag.text if not (tag.text in "MIRÃ TAMBIÃN") else "" for tag in content_tag])
        return title, subtitle, content
    except requests.RequestException as e:
        print(f"Error al cargar la página de TyC Sports: {e}")
        return None