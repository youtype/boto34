"""
Wrapper for boto3 DirectoryService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ds/)

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
    # Returns type annotated boto3 DirectoryService client
    ds_client = session.ds.client()
    ds_client: types_boto3_ds.client.DirectoryServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ds.client import DirectoryServiceClient
except ImportError:
    DirectoryServiceClient = object  # type: ignore[misc,assignment]


class DirectoryServiceService(
    ServiceFactory[DirectoryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ds"
    _SERVICE_PROP = "ds"
