"""
Wrapper for aioboto3 RePostPrivate service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_repostspace/)

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
    # Returns type annotated aioboto3 RePostPrivate client
    repostspace_client = session.repostspace.client()
    repostspace_client: types_aiobotocore_repostspace.client.RePostPrivateClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_repostspace.client import RePostPrivateClient

from boto34.aioboto3.service_factory import ServiceFactory


class RePostPrivateService(ServiceFactory[RePostPrivateClient]):
    SERVICE_NAME = "repostspace"
    _SERVICE_PROP = "repostspace"
