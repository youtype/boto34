"""
Wrapper for aiobotocore GreengrassV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_greengrassv2/)

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
    # Returns type annotated aiobotocore GreengrassV2 client
    async with session.greengrassv2.create_client() as greengrassv2_client:
        greengrassv2_client: types_aiobotocore_greengrassv2.client.GreengrassV2Client
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_greengrassv2.client import GreengrassV2Client
except ImportError:
    GreengrassV2Client = object  # type: ignore[misc,assignment]


class GreengrassV2Service(
    ServiceFactory[GreengrassV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "greengrassv2"
    _SERVICE_PROP = "greengrassv2"
