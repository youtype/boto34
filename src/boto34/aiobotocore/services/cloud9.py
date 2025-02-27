"""
Wrapper for aiobotocore Cloud9 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloud9/)

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
    # Returns type annotated aiobotocore Cloud9 client
    async with session.cloud9.create_client() as cloud9_client:
        cloud9_client: types_aiobotocore_cloud9.client.Cloud9Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloud9.client import Cloud9Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloud9.client import Cloud9Client
except ImportError:
    Cloud9Client = object  # type: ignore[misc,assignment]


class Cloud9Service(
    ServiceFactory[Cloud9Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloud9"
    _SERVICE_PROP = "cloud9"
