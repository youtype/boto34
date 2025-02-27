"""
Wrapper for aiobotocore ElasticsearchService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_es/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ElasticsearchService client
    async with session.es.create_client() as es_client:
        es_client: types_aiobotocore_es.client.ElasticsearchServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_es.client import ElasticsearchServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ElasticsearchServiceService(ServiceFactory[ElasticsearchServiceClient]):
    SERVICE_NAME = "es"
    _SERVICE_PROP = "es"
