"""
Wrapper for aioboto3 CodeStarconnections service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codestar_connections/)

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
    # Returns type annotated aioboto3 CodeStarconnections client
    codestar_connections_client = session.codestar_connections.client()
    codestar_connections_client: types_aiobotocore_codestar_connections.client.CodeStarconnectionsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codestar_connections.client import CodeStarconnectionsClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeStarconnectionsService(ServiceFactory[CodeStarconnectionsClient]):
    SERVICE_NAME = "codestar-connections"
    _SERVICE_PROP = "codestar_connections"
