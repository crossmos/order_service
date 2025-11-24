import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    ORDERS_TOPIC: str = "orders"
    PRODUCER_CLIENT_ID: str = "order-service-producer"


settings = Settings()


# Базовая настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Логгер для order-service
order_logger = logging.getLogger("order-service")
