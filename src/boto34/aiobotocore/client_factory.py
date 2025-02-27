from typing import Generic, TypeVar

from botocore.client import BaseClient

_Client = TypeVar("_Client", bound=BaseClient)


class ClientFactory(Generic[_Client]):
    def __init__(self, client: _Client) -> None:
        self._client = client
