FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /api

COPY ./app /api/app

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        poppler-utils \
        tesseract-ocr \
        tesseract-ocr-osd \
        tesseract-ocr-spa

COPY requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r /api/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80