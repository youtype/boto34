"""
Wrapper for aiobotocore KMS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kms/)

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
    # Returns type annotated aiobotocore KMS client
    async with session.kms.create_client() as kms_client:
        kms_client: types_aiobotocore_kms.client.KMSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kms.client import KMSClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kms.client import KMSClient
except ImportError:
    KMSClient = object  # type: ignore[misc,assignment]


class KMSService(
    ServiceFactory[KMSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kms"
    _SERVICE_PROP = "kms"
