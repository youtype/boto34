"""
Wrapper for aioboto3 Athena service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_athena/)

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
    # Returns type annotated aioboto3 Athena client
    athena_client = session.athena.client()
    athena_client: types_aiobotocore_athena.client.AthenaClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_athena.client import AthenaClient
except ImportError:
    AthenaClient = object  # type: ignore[misc,assignment]


class AthenaService(
    ServiceFactory[AthenaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "athena"
    _SERVICE_PROP = "athena"
