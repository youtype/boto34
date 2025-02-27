"""
Wrapper for aiobotocore CloudTrailDataService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudtrail_data/)

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
    # Returns type annotated aiobotocore CloudTrailDataService client
    async with session.cloudtrail_data.create_client() as cloudtrail_data_client:
        cloudtrail_data_client: types_aiobotocore_cloudtrail_data.client.CloudTrailDataServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudtrail_data.client import CloudTrailDataServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudtrail_data.client import CloudTrailDataServiceClient
except ImportError:
    CloudTrailDataServiceClient = object  # type: ignore[misc,assignment]


class CloudTrailDataServiceService(
    ServiceFactory[CloudTrailDataServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudtrail-data"
    _SERVICE_PROP = "cloudtrail_data"
