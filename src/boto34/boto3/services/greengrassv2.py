"""
Wrapper for boto3 GreengrassV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_greengrassv2/)

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
    # Returns type annotated boto3 GreengrassV2 client
    greengrassv2_client = session.greengrassv2.client()
    greengrassv2_client: types_boto3_greengrassv2.client.GreengrassV2Client
    ```
"""

from __future__ import annotations

from types_boto3_greengrassv2.client import GreengrassV2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_greengrassv2.client import GreengrassV2Client
except ImportError:
    GreengrassV2Client = object  # type: ignore[misc,assignment]


class GreengrassV2Service(
    ServiceFactory[GreengrassV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "greengrassv2"
    _SERVICE_PROP = "greengrassv2"
