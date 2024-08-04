# BocaMarketMonitor AI

**BocaMarketMonitor AI** es una herramienta avanzada diseñada para analizar noticias relacionadas con el mercado de transferencias en el fútbol, específicamente para el Club Atlético Boca Juniors. Utiliza técnicas de web scraping y la API de Gemini para extraer y procesar información de varias fuentes de noticias. La herramienta calcula la probabilidad de que un jugador se transfiera de un equipo a otro y proporciona un resumen detallado de cada artículo.

## Características

- **Web Scraping:** Extrae información de artículos de noticias desde sitios web como:
  - [Bolavip](https://www.bolavip.com)
  - [TyC Sports](https://www.tycsports.com/boca-juniors)
  - [Planeta Boca Juniors](https://www.planetabj.com)
  
- **Análisis de Noticias:** Utiliza la API de Gemini para analizar el contenido de los artículos y determinar la probabilidad de transferencia de jugadores.
  
- **Resumen de Artículos:** Genera un resumen claro y conciso del contenido de cada noticia.

- **API Propia:** Proporciona una API para conectar con el sistema de web scraping y acceder a los datos procesados.

## Instalación

Para comenzar a usar **BocaMarketMonitor AI**, sigue estos pasos:

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/cr4t3/BocaMarketMonitor-AI.git
    ```

2. **Navega al directorio del proyecto:**
    ```bash
    cd BocaMarketMonitor-AI
    ```

3. **Crea un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configura las credenciales de la API de Gemini:**
   - Accede a la pagina de [API de Gemini](https://aistudio.google.com/app/apikey) y obtiene una key a base de un nuevo proyecto
   - Crea un archivo `.env` en la raíz del proyecto y agrega tus credenciales y link a la API preinstalada:
     ```
     GEMINI_API_KEY=tu_clave_de_api
     NEWS_API=link_de_la_api
     ```

## Uso

1. **Ejecuta el servidor de la API:**
    ```bash
    python api.py
    ```

2. **Accede a la API:**
   - **Endpoint General:** `http://localhost:5000/getall/*`  
     Obtiene noticias de todas las fuentes configuradas.
   - **Endpoint Específico para Bolavip:** `http://localhost:5000/getall/bolavip`  
   - **Endpoint Específico para TyC Sports:** `http://localhost:5000/getall/tycsports`  
   - **Endpoint Específico para Planeta Boca Juniors:** `http://localhost:5000/getall/planetabj`  

3. **¿Qué es la API?**
   - La API webscrapea la página dependiendo de su código HTML analizado previamente. Devuelve los resultados del web scraping de forma más organizada.

## Por hacer

- [ ] **Mejorar el análisis de probabilidad de transferencia:** Optimizar el algoritmo para aumentar la precisión.
- [ ] **Agregar más fuentes de noticias:** Incluir sitios web adicionales para ampliar el rango de información.
- [ ] **Desarrollar una interfaz gráfica de usuario (GUI):** Facilitar el uso de la herramienta a través de una interfaz amigable.
- [ ] **Implementar un sistema de notificaciones:** Alertar a los usuarios sobre noticias relevantes o cambios en las probabilidades de transferencia por E-Mail.
- [ ] **Optimizar el rendimiento del web scraping:** Reducir el tiempo de respuesta y mejorar la eficiencia del scraping.
- [ ] **Manejo de errores:** Agregar manejos de errores en mas lugares
- [ ] **Agregar cache:** Al agregar cache en disco se tendria que mejorar la velocidad del programa
- [ ] **Agregar seguridad a la API:** Agregar seguridad a la API para evitar mal usos
- [ ] **Mover AI a la API:** Mover la AI a la API para poder permitir utilizacion por parte de otros programas
- [ ] **Agregar guia de estilo:** Agregar guia de estilo para facilitar el desarollo
- [ ] **Crear documentacion:** Crear documentacion para usar BocaMarketMonitor AI

## Contribución

Si deseas contribuir a **BocaMarketMonitor AI**, por favor sigue estos pasos:

1. **Haz un fork del repositorio.**
2. **Crea una nueva rama para tu característica o corrección de errores:**
    ```bash
    git checkout -b mi-nueva-caracteristica
    ```
3. **Realiza tus cambios y haz commits:**
    ```bash
    git commit -am 'Agregué una nueva característica'
    ```
4. **Empuja tus cambios a tu fork:**
    ```bash
    git push origin mi-nueva-caracteristica
    ```
5. **Envía una solicitud de extracción (pull request).**

## Licencia

Este proyecto está licenciado bajo la [Licencia Apache 2.0](LICENSE).

## Contacto

Para preguntas o soporte, contacta a [crate.arg@proton.me](mailto:crate.arg@proton.me).
