import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(".env")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

  # Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


def filter_links(links: tuple[str]):
  chat_session = model.start_chat(
    history=[
    ]
  )
  return chat_session.send_message(f"""A continuación, se te proporcionará una lista de URLs de artículos de noticias sobre Boca Juniors. Tu tarea es analizar estas URLs y devolver solo aquellas que están relacionadas con el mercado de pases (transferencias, fichajes, ventas, contrataciones, etc.), pero solo si se habla de Boca que va a recibir o pierder un jugador. Si el titulo habla de un resumen del mercado de pases, pero no de posibles fichajes, no lo incluyas. Nada mas de fichajes de JUGADORES, no de entrenadores o ex-jugadores.
Lista de URLs:
["{"\",\n".join(list(links))}]

Devuelve un JSON con el siguiente formato:

{'{'}
  "market_transfer_links": [    "URL del artículo relacionado con el mercado de pases 1",    "URL del artículo relacionado con el mercado de pases 2",    "URL del artículo relacionado con el mercado de pases 3"  ]
{'}'}
""").text

def player_data(title: str, subtitle: str, content: str):
  chat_session = model.start_chat(
    history=[
    ]
  )
  return chat_session.send_message(f"""A continuación, se te proporcionará el contenido de un artículo relacionado con un fichaje o cesión de o para Boca Juniors. Tu tarea es analizar el contenido y devolver un JSON con la siguiente estructura:

{'{'}
  "player_name": "Nombre del jugador",
  "from": "Nombre del equipo del que se está transfiriendo el jugador",
  "to": "Nombre del equipo al que se está transfiriendo el jugador",
  "possibilities": Que tan posible es el fichaje (0 siendo imposible, 100 siendo confirmado),
  "summary": "Resumen del artículo sobre la transferencia"
{'}'}

Contenido del articulo:
Titulo: {title}
Subtitulo: {subtitle}
Contenido: {content}

Asegúrate de proporcionar la información precisa y relevante. No incluyas explicaciones o detalles adicionales en la respuesta.
""").text