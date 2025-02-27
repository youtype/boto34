"""
Wrapper for aioboto3 FreeTier service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_freetier/)

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
    # Returns type annotated aioboto3 FreeTier client
    freetier_client = session.freetier.client()
    freetier_client: types_aiobotocore_freetier.client.FreeTierClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_freetier.client import FreeTierClient
except ImportError:
    FreeTierClient = object  # type: ignore[misc,assignment]


class FreeTierService(
    ServiceFactory[FreeTierClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "freetier"
    _SERVICE_PROP = "freetier"
