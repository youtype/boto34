from aiobotocore.client import AioBaseClient
from aiobotocore.waiter import AIOWaiter


class WaiterFactory:
    def __init__(self, client: AioBaseClient) -> None:
        self._client = client

    def get_waiter(self, waiter_name: str) -> AIOWaiter:
        self._client.get_waiter(waiter_name)
