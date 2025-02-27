"""
Wrapper for boto3 Cloud9 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloud9/)

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
    # Returns type annotated boto3 Cloud9 client
    cloud9_client = session.cloud9.client()
    cloud9_client: types_boto3_cloud9.client.Cloud9Client
    ```
"""

from __future__ import annotations

from types_boto3_cloud9.client import Cloud9Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloud9.client import Cloud9Client
except ImportError:
    Cloud9Client = object  # type: ignore[misc,assignment]


class Cloud9Service(
    ServiceFactory[Cloud9Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloud9"
    _SERVICE_PROP = "cloud9"
