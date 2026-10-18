import os
import sys

from fastapi.testclient import TestClient

ORDERS_PATH = os.environ.get(
    "ORDERS_SERVICE_PATH",
    os.path.join(os.path.dirname(__file__), "..", "orders-service"),
)
sys.path.insert(0, ORDERS_PATH)

from main import app  # the real orders-service app  # noqa: E402

from billing import client as billing  # noqa: E402

http = TestClient(app)


def test_get_customer_name():
    assert billing.get_customer_name(1, http) == "Asha"


def test_get_order_total():
    assert billing.get_order_total(1, http) == 499.0
