FROM python:3.11

WORKDIR /order_service

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "-m", "src.main"]