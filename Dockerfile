FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY run.py .

EXPOSE 8080

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${WEBSITES_PORT:-8080} --timeout 120 --workers 4 run:app"]
