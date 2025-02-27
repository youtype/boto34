"""
Wrapper for aioboto3 ElasticsearchService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_es/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ElasticsearchService client
    es_client = session.es.client()
    es_client: types_aiobotocore_es.client.ElasticsearchServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_es.client import ElasticsearchServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ElasticsearchServiceService(ServiceFactory[ElasticsearchServiceClient]):
    SERVICE_NAME = "es"
    _SERVICE_PROP = "es"
