import uuid
import json

import pytest


@pytest.fixture
def order_json():
    order = {
        "order_id": str(uuid.uuid4()),
        "user_id": "user_1",
        "item": "widget",
        "quantity": 1 % 5 + 1,
    }

    order_json = json.dumps(order)
    return order_json
