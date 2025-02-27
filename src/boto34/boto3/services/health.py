"""
Wrapper for boto3 Health service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_health/)

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
    # Returns type annotated boto3 Health client
    health_client = session.health.client()
    health_client: types_boto3_health.client.HealthClient
    ```
"""

from __future__ import annotations

from types_boto3_health.client import HealthClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_health.client import HealthClient
except ImportError:
    HealthClient = object  # type: ignore[misc,assignment]


class HealthService(
    ServiceFactory[HealthClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "health"
    _SERVICE_PROP = "health"
