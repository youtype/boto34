from botocore.client import BaseClient
from botocore.waiter import Waiter


class WaiterFactory:
    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def get_waiter(self, waiter_name: str) -> Waiter:
        self._client.get_waiter(waiter_name)
