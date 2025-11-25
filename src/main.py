from contextlib import asynccontextmanager

import uvicorn
from confluent_kafka.admin import AdminClient, NewTopic
from fastapi import FastAPI

from src.routers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # shutdown
    pass


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(api_router)


if __name__ == "__main__":
    admin = AdminClient({"bootstrap.servers": "kafka:9092"})
    topics = [
        NewTopic("orders", num_partitions=1, replication_factor=1),
        NewTopic("notifications", num_partitions=1, replication_factor=1),
    ]

    fs = admin.create_topics(topics)

    for topic, f in fs.items():
        try:
            f.result()
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Topic {topic} already exists: {e}")

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
    )
