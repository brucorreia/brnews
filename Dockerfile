FROM python:3.10.5-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x start.sh

CMD ["sh", "-c", "/app/start.sh"]