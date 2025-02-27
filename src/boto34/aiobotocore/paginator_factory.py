from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator


class PaginatorFactory:
    def __init__(self, client: AioBaseClient) -> None:
        self._client = client

    def get_paginator(self, paginator_name: str) -> AioPaginator:
        self._client.get_paginator(paginator_name)
