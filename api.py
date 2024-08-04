from flask import Flask, jsonify, make_response, abort
import utils  # Asegúrate de que las funciones de carga están en el módulo utils

app = Flask(__name__)

@app.route("/getall/<site>", methods=["GET"])
def get_all(site: str):
    match site:
        case "tycsports":
            urls = utils.get_tycsports_news_urls()
        case "planetabj":
            urls = utils.get_planetabj_news_urls()
        case "bolavip":
            urls = utils.get_bolavip_news_urls()
        case "*":
            urls = utils.get_all_news_urls()
        case _:
            return abort(404)
    
    return make_response(jsonify(urls), 200)

@app.route("/get/<site>/<page>", methods=["GET"])
def get_news(site: str, page: str):
    url_mapping = {
        "planetabj": utils.load_planetabj_page,
        "bolavip": utils.load_bolavip_page,
        "tycsports": utils.load_tycsports_page
    }
    
    base_url_mapping = {
        "planetabj": "https://planetabj.com/boca-juniors",
        "bolavip": "https://bolavip.com/ar/boca",
        "tycsports": "https://www.tycsports.com/boca-juniors"
    }
    
    if site not in url_mapping:
        return jsonify({"error": "Unsupported site"}), 400
    
    base_url = base_url_mapping[site]
    url = f"{base_url}/{page}"
    
    # Cargar la página y obtener el contenido
    try:
        title, subtitle, content = url_mapping[site](url)
    except Exception as e:
        return jsonify({"error": f"Failed to load page: {str(e)}"}), 500
    
    return jsonify({
        "title": title,
        "subtitle": subtitle,
        "content": content
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
