import httpx


def get_customer_name(order_id: int, client: httpx.Client) -> str:
    r = client.get(f"/orders/{order_id}")
    r.raise_for_status()
    return r.json()["customer_name"]


def get_order_total(order_id: int, client: httpx.Client) -> float:
    r = client.get(f"/orders/{order_id}")
    r.raise_for_status()
    return r.json()["total"]
