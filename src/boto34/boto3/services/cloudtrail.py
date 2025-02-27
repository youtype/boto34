"""
Wrapper for boto3 CloudTrail service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CloudTrail client
    cloudtrail_client = session.cloudtrail.client()
    cloudtrail_client: types_boto3_cloudtrail.client.CloudTrailClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloudtrail.client import CloudTrailClient
except ImportError:
    CloudTrailClient = object  # type: ignore[misc,assignment]


class CloudTrailService(
    ServiceFactory[CloudTrailClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudtrail"
    _SERVICE_PROP = "cloudtrail"
