"""
Wrapper for boto3 FinSpaceData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_finspace_data/)

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
    # Returns type annotated boto3 FinSpaceData client
    finspace_data_client = session.finspace_data.client()
    finspace_data_client: types_boto3_finspace_data.client.FinSpaceDataClient
    ```
"""

from __future__ import annotations

from types_boto3_finspace_data.client import FinSpaceDataClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_finspace_data.client import FinSpaceDataClient
except ImportError:
    FinSpaceDataClient = object  # type: ignore[misc,assignment]


class FinSpaceDataService(
    ServiceFactory[FinSpaceDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "finspace-data"
    _SERVICE_PROP = "finspace_data"
