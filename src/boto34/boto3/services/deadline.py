"""
Wrapper for boto3 DeadlineCloud service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_deadline/)

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
    # Returns type annotated boto3 DeadlineCloud client
    deadline_client = session.deadline.client()
    deadline_client: types_boto3_deadline.client.DeadlineCloudClient
    ```
"""

from __future__ import annotations

from types_boto3_deadline.client import DeadlineCloudClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_deadline.client import DeadlineCloudClient
except ImportError:
    DeadlineCloudClient = object  # type: ignore[misc,assignment]


class DeadlineCloudService(
    ServiceFactory[DeadlineCloudClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "deadline"
    _SERVICE_PROP = "deadline"
