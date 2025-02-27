"""
Wrapper for boto3 CleanRoomsML service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cleanroomsml/)

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
    # Returns type annotated boto3 CleanRoomsML client
    cleanroomsml_client = session.cleanroomsml.client()
    cleanroomsml_client: types_boto3_cleanroomsml.client.CleanRoomsMLClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cleanroomsml.client import CleanRoomsMLClient
except ImportError:
    CleanRoomsMLClient = object  # type: ignore[misc,assignment]


class CleanRoomsMLService(
    ServiceFactory[CleanRoomsMLClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cleanroomsml"
    _SERVICE_PROP = "cleanroomsml"
