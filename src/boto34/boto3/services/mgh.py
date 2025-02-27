"""
Wrapper for boto3 MigrationHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mgh/)

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
    # Returns type annotated boto3 MigrationHub client
    mgh_client = session.mgh.client()
    mgh_client: types_boto3_mgh.client.MigrationHubClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mgh.client import MigrationHubClient
except ImportError:
    MigrationHubClient = object  # type: ignore[misc,assignment]


class MigrationHubService(
    ServiceFactory[MigrationHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mgh"
    _SERVICE_PROP = "mgh"
