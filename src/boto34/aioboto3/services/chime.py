"""
Wrapper for aioboto3 Chime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime/)

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
    # Returns type annotated aioboto3 Chime client
    chime_client = session.chime.client()
    chime_client: types_aiobotocore_chime.client.ChimeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chime.client import ChimeClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChimeService(ServiceFactory[ChimeClient]):
    SERVICE_NAME = "chime"
    _SERVICE_PROP = "chime"
