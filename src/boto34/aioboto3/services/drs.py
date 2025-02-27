"""
Wrapper for aioboto3 Drs service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_drs/)

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
    # Returns type annotated aioboto3 Drs client
    drs_client = session.drs.client()
    drs_client: types_aiobotocore_drs.client.DrsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_drs.client import DrsClient
except ImportError:
    DrsClient = object  # type: ignore[misc,assignment]


class DrsService(
    ServiceFactory[DrsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "drs"
    _SERVICE_PROP = "drs"
