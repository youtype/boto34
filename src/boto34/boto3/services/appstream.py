"""
Wrapper for boto3 AppStream service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appstream/)

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
    # Returns type annotated boto3 AppStream client
    appstream_client = session.appstream.client()
    appstream_client: types_boto3_appstream.client.AppStreamClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_appstream.client import AppStreamClient
except ImportError:
    AppStreamClient = object  # type: ignore[misc,assignment]


class AppStreamService(
    ServiceFactory[AppStreamClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appstream"
    _SERVICE_PROP = "appstream"
