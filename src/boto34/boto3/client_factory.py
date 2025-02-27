"""
Proxy class that wraps botocore.BaseClient.

Copyright 2025 Vlad Emelianov
"""

from typing import Generic, TypeVar

from botocore.client import BaseClient

_Client = TypeVar("_Client", bound=BaseClient)


class ClientFactory(Generic[_Client]):
    """
    Proxy class that wraps a boto3 Client.
    """

    def __init__(self, client: _Client) -> None:
        self._client = client
