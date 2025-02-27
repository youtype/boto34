"""
Wrapper for aioboto3 CloudTrail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudtrail/)

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
    # Returns type annotated aioboto3 CloudTrail client
    cloudtrail_client = session.cloudtrail.client()
    cloudtrail_client: types_aiobotocore_cloudtrail.client.CloudTrailClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudtrail.client import CloudTrailClient
except ImportError:
    CloudTrailClient = object  # type: ignore[misc,assignment]


class CloudTrailService(
    ServiceFactory[CloudTrailClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudtrail"
    _SERVICE_PROP = "cloudtrail"
