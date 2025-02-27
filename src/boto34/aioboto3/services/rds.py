"""
Wrapper for aioboto3 RDS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rds/)

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
    # Returns type annotated aioboto3 RDS client
    rds_client = session.rds.client()
    rds_client: types_aiobotocore_rds.client.RDSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_rds.client import RDSClient
except ImportError:
    RDSClient = object  # type: ignore[misc,assignment]


class RDSService(
    ServiceFactory[RDSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rds"
    _SERVICE_PROP = "rds"
