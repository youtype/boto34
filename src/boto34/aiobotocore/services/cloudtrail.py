"""
Wrapper for aiobotocore CloudTrail service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudtrail/)

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
    # Returns type annotated aiobotocore CloudTrail client
    async with session.cloudtrail.create_client() as cloudtrail_client:
        cloudtrail_client: types_aiobotocore_cloudtrail.client.CloudTrailClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudtrail.client import CloudTrailClient
except ImportError:
    CloudTrailClient = object  # type: ignore[misc,assignment]


class CloudTrailService(
    ServiceFactory[CloudTrailClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudtrail"
    _SERVICE_PROP = "cloudtrail"
