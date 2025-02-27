"""
Wrapper for aiobotocore OpenSearchServiceServerless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/)

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
    # Returns type annotated aiobotocore OpenSearchServiceServerless client
    async with session.opensearchserverless.create_client() as opensearchserverless_client:
        opensearchserverless_client: (
            types_aiobotocore_opensearchserverless.client.OpenSearchServiceServerlessClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_opensearchserverless.client import OpenSearchServiceServerlessClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpenSearchServiceServerlessService(ServiceFactory[OpenSearchServiceServerlessClient]):
    SERVICE_NAME = "opensearchserverless"
    _SERVICE_PROP = "opensearchserverless"
