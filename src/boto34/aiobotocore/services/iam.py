"""
Wrapper for aiobotocore IAM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iam/)

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
    # Returns type annotated aiobotocore IAM client
    async with session.iam.create_client() as iam_client:
        iam_client: types_aiobotocore_iam.client.IAMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iam.client import IAMClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iam.client import IAMClient
except ImportError:
    IAMClient = object  # type: ignore[misc,assignment]


class IAMService(
    ServiceFactory[IAMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iam"
    _SERVICE_PROP = "iam"
