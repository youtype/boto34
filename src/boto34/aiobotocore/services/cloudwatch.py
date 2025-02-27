"""
Wrapper for aiobotocore CloudWatch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/)

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
    # Returns type annotated aiobotocore CloudWatch client
    async with session.cloudwatch.create_client() as cloudwatch_client:
        cloudwatch_client: types_aiobotocore_cloudwatch.client.CloudWatchClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudwatch.client import CloudWatchClient
except ImportError:
    CloudWatchClient = object  # type: ignore[misc,assignment]


class CloudWatchService(
    ServiceFactory[CloudWatchClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudwatch"
    _SERVICE_PROP = "cloudwatch"
