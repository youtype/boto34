"""
Wrapper for boto3 Snowball service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_snowball/)

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
    # Returns type annotated boto3 Snowball client
    snowball_client = session.snowball.client()
    snowball_client: types_boto3_snowball.client.SnowballClient
    ```
"""

from __future__ import annotations

from types_boto3_snowball.client import SnowballClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_snowball.client import SnowballClient
except ImportError:
    SnowballClient = object  # type: ignore[misc,assignment]


class SnowballService(
    ServiceFactory[SnowballClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "snowball"
    _SERVICE_PROP = "snowball"
