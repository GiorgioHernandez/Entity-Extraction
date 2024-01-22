# Extracción de entidades usando Large Language Models (LLM)

La metodología y ejecución de este proyecto se divide en: 

    1. Reconocimiento de texto usando Unstructured

        Para hacer uso de los grandes modelos del lenguaje, como ChatGPT de OpenAI es necesario suministrar un contexto, el cuál debe ser extraído de los archivos (pdfs, imágenes). Para ello, se hace uso de "Unstructured" https://unstructured-io.github.io/unstructured/index.html .

        Básicamente, Unstructured utiliza un modelo de reconocimiento de carácteres óptico (OCR-tesseract) para extraer el texto y un modelo de detección de objetos (Yolo) para la extracción de elementos (ejemplo: tablas).

        IMPORTANTE: La calidad de extracción del texto depende de la calidad de las imágenes. 

    2. Extracción de entidades (LLM)

        Los grandes modelos del lenguaje han sido entrenados para procesar órdenes a partir de texto, como es el caso de GPT3.5 o GPT4. 

        Cada uno de estos modelos es capaz de recibir instrucciones de texto para cumplir una tarea específica. Esto es posible gracias a la configuración de prompts, queries y uso de chains que ejecutan el modelo con un contexto específico. Todo lo anterior, es desarrollado con Langchain https://python.langchain.com/docs/get_started/introduction 

        Cada modelo tiene un límite en la ventana de contexto, medido en cantidad de tokens. Según aumenta la cantidad de tokens que puede recibir el modelo, aumenta el precio.
            GPT3.5, recibe 4k a 16k tokens
            GPT4, recibe hasta 128k tokens
        Ya que los archivos no contienen mucho texto, para este proyecto es usado una ventana de contexto de hasta 4k tokens. 

        Nota: recientemente, han sido lanzados nuevos modelos que son capaces de procesar texto, imágenes y audio, es decir, multimodales. Estos son conocidos como LMM (Large Multimodal Models). Como por ejemplo el reciente GPT4-V.

    3. Despliegue:

        Se recomienda el uso de Docker para evitar problemas de dependencias o de sistema operativo, el repositorio ya incluye los archivos correspondientes para el uso de Docker, los comandos necesarios son:

        Construir imagen: 
            docker build -t llm-v1 

        Run:
            docker-compose up

## Dentro de la estructura del proyecto se pueden encontrar distintos archivos:

    1. inference.py : se encarga de crear e iniciar la clase Process.
    2. main.py : es el archivo que inicializa la API.
    3. fields.py : aquí se especifican los campos que se le solicita extrer a ChatGPT.
    4. enums.py : en este archivo se enumeran las posibles categorias de algunos campos (como tipo de documento, etc.).
    5. request.py : este archivo se utiliza para pruebas, en escencia se encarga de hacer múltiples solicitudes a la API y guarda su respectiva salida en archivos JSON.
    6. tablas.py : este archivo se utiliza para pruebas, se encarga de tomar los archivos JSON generados por request.py y crea una tabla CSV con todas las extracciones.

## Existe un único método para utilizar la API:

    método: http://0.0.0.0:8080/api/extraction

    curl -X 'POST' \
    'http://localhost:8080/api/extraction' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'file=@FILENAME.jpeg;type=image/jpeg'

## Quickstart:
    
    1. Es importante tener una cuenta de github para clonar el repositorio, basta con ir a https://github.com/ y crear una cuenta mediante el botón "sign up". Luego de esto, deberán contactar al desarrollador para brindar acceso a la nueva cuenta creada, y poder clonarlo. 

    2. Así mismo, es necesario tener una cuenta en el portal de OpenAI, aquí podrán gestionar el saldo destinado a la extracción de entidades. en https://openai.com/ el botón "log in" permite ir a la pantalla de inicio de sesión o de creación de cuenta. Más adelante, en el botón de API, entrarán a la pantalla de administración de los servicios de OpenAI. En el banner de la derecha, en el apartado de Settings>Billing, podrán gestionar los métodos de pago y el saldo actual. Ahora, en el apartado de API Keys, podrán generar el número secreto de la API, este número es sumamente importante, pues es por medio del cual este desarrollo puede integrarse con Chat GPT. 

    3. Una vez obtenido el API Key, debe ser incluído en el archivo "inference.py" en la línea 19. 


## Trabajo Futuro:

    Es necesario la creación de un software que se alimente de esta API y se integre con el software de agendamiento de citas MEDIFOLIOS, la idea es llenar los campos automáticamente al subir una (o varias) imágen(es). 
 