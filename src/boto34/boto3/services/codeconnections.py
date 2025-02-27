"""
Wrapper for boto3 CodeConnections service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeconnections/)

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
    # Returns type annotated boto3 CodeConnections client
    codeconnections_client = session.codeconnections.client()
    codeconnections_client: types_boto3_codeconnections.client.CodeConnectionsClient
    ```
"""

from __future__ import annotations

from types_boto3_codeconnections.client import CodeConnectionsClient

from boto34.boto3.service_factory import ServiceFactory


class CodeConnectionsService(ServiceFactory[CodeConnectionsClient]):
    SERVICE_NAME = "codeconnections"
    _SERVICE_PROP = "codeconnections"
