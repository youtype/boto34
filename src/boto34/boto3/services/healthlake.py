"""
Wrapper for boto3 HealthLake service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_healthlake/)

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
    # Returns type annotated boto3 HealthLake client
    healthlake_client = session.healthlake.client()
    healthlake_client: types_boto3_healthlake.client.HealthLakeClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_healthlake.client import HealthLakeClient
except ImportError:
    HealthLakeClient = object  # type: ignore[misc,assignment]


class HealthLakeService(
    ServiceFactory[HealthLakeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "healthlake"
    _SERVICE_PROP = "healthlake"
