import logging

from pydantic_settings import BaseSettings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

order_logger = logging.getLogger("order-service")


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"
    ORDERS_TOPIC: str = "orders"
    PRODUCER_CLIENT_ID: str = "order-service-producer"


settings = Settings()
