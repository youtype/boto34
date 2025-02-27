"""
Wrapper for boto3 CodeStarconnections service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_connections/)

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
    # Returns type annotated boto3 CodeStarconnections client
    codestar_connections_client = session.codestar_connections.client()
    codestar_connections_client: types_boto3_codestar_connections.client.CodeStarconnectionsClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_codestar_connections.client import CodeStarconnectionsClient
except ImportError:
    CodeStarconnectionsClient = object  # type: ignore[misc,assignment]


class CodeStarconnectionsService(
    ServiceFactory[CodeStarconnectionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codestar-connections"
    _SERVICE_PROP = "codestar_connections"
