from botocore.client import BaseClient
from botocore.paginate import Paginator


class PaginatorFactory:
    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def get_paginator(self, paginator_name: str) -> Paginator:
        self._client.get_paginator(paginator_name)
