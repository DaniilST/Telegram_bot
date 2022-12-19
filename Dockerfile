FROM python:3.7

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ../../../Documents/Downloads/Telegram%20Desktop .

CMD ["python3", "main.py"]
