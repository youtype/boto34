"""
Wrapper for aiobotocore CloudWatchObservabilityAccessManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/)

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
    # Returns type annotated aiobotocore CloudWatchObservabilityAccessManager client
    async with session.oam.create_client() as oam_client:
        oam_client: types_aiobotocore_oam.client.CloudWatchObservabilityAccessManagerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_oam.client import CloudWatchObservabilityAccessManagerClient
except ImportError:
    CloudWatchObservabilityAccessManagerClient = object  # type: ignore[misc,assignment]


class CloudWatchObservabilityAccessManagerService(
    ServiceFactory[CloudWatchObservabilityAccessManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "oam"
    _SERVICE_PROP = "oam"
