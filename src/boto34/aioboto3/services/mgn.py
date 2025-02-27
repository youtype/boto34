"""
Wrapper for aioboto3 Mgn service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mgn/)

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
    # Returns type annotated aioboto3 Mgn client
    mgn_client = session.mgn.client()
    mgn_client: types_aiobotocore_mgn.client.MgnClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_mgn.client import MgnClient
except ImportError:
    MgnClient = object  # type: ignore[misc,assignment]


class MgnService(
    ServiceFactory[MgnClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mgn"
    _SERVICE_PROP = "mgn"
