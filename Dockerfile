FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY modelo ./modelo
COPY start.sh ./start.sh

RUN chmod +x ./start.sh

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "./start.sh"]