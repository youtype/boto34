"""
Wrapper for aiobotocore Detective service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_detective/)

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
    # Returns type annotated aiobotocore Detective client
    async with session.detective.create_client() as detective_client:
        detective_client: types_aiobotocore_detective.client.DetectiveClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_detective.client import DetectiveClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DetectiveService(ServiceFactory[DetectiveClient]):
    SERVICE_NAME = "detective"
    _SERVICE_PROP = "detective"
