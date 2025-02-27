"""
Wrapper for aioboto3 Neptune service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptune/)

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
    # Returns type annotated aioboto3 Neptune client
    neptune_client = session.neptune.client()
    neptune_client: types_aiobotocore_neptune.client.NeptuneClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_neptune.client import NeptuneClient
except ImportError:
    NeptuneClient = object  # type: ignore[misc,assignment]


class NeptuneService(
    ServiceFactory[NeptuneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "neptune"
    _SERVICE_PROP = "neptune"
