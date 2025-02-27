"""
Wrapper for aioboto3 CodeCatalyst service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codecatalyst/)

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
    # Returns type annotated aioboto3 CodeCatalyst client
    codecatalyst_client = session.codecatalyst.client()
    codecatalyst_client: types_aiobotocore_codecatalyst.client.CodeCatalystClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codecatalyst.client import CodeCatalystClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeCatalystService(ServiceFactory[CodeCatalystClient]):
    SERVICE_NAME = "codecatalyst"
    _SERVICE_PROP = "codecatalyst"
