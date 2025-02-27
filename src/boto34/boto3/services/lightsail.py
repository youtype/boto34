"""
Wrapper for boto3 Lightsail service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lightsail/)

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
    # Returns type annotated boto3 Lightsail client
    lightsail_client = session.lightsail.client()
    lightsail_client: types_boto3_lightsail.client.LightsailClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_lightsail.client import LightsailClient
except ImportError:
    LightsailClient = object  # type: ignore[misc,assignment]


class LightsailService(
    ServiceFactory[LightsailClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lightsail"
    _SERVICE_PROP = "lightsail"
