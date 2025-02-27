"""
Wrapper for aioboto3 CloudTrailDataService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudtrail_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CloudTrailDataService client
    cloudtrail_data_client = session.cloudtrail_data.client()
    cloudtrail_data_client: types_aiobotocore_cloudtrail_data.client.CloudTrailDataServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudtrail_data.client import CloudTrailDataServiceClient
except ImportError:
    CloudTrailDataServiceClient = object  # type: ignore[misc,assignment]


class CloudTrailDataServiceService(
    ServiceFactory[CloudTrailDataServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudtrail-data"
    _SERVICE_PROP = "cloudtrail_data"
