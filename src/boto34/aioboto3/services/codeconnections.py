"""
Wrapper for aioboto3 CodeConnections service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeconnections/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CodeConnections client
    codeconnections_client = session.codeconnections.client()
    codeconnections_client: types_aiobotocore_codeconnections.client.CodeConnectionsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codeconnections.client import CodeConnectionsClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeConnectionsService(ServiceFactory[CodeConnectionsClient]):
    SERVICE_NAME = "codeconnections"
    _SERVICE_PROP = "codeconnections"
