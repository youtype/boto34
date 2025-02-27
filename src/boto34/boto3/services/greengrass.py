"""
Wrapper for boto3 Greengrass service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_greengrass/)

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
    # Returns type annotated boto3 Greengrass client
    greengrass_client = session.greengrass.client()
    greengrass_client: types_boto3_greengrass.client.GreengrassClient
    ```
"""

from __future__ import annotations

from types_boto3_greengrass.client import GreengrassClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_greengrass.client import GreengrassClient
except ImportError:
    GreengrassClient = object  # type: ignore[misc,assignment]


class GreengrassService(
    ServiceFactory[GreengrassClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "greengrass"
    _SERVICE_PROP = "greengrass"
