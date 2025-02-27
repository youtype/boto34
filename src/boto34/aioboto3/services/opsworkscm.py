"""
Wrapper for aioboto3 OpsWorksCM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opsworkscm/)

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
    # Returns type annotated aioboto3 OpsWorksCM client
    opsworkscm_client = session.opsworkscm.client()
    opsworkscm_client: types_aiobotocore_opsworkscm.client.OpsWorksCMClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_opsworkscm.client import OpsWorksCMClient
except ImportError:
    OpsWorksCMClient = object  # type: ignore[misc,assignment]


class OpsWorksCMService(
    ServiceFactory[OpsWorksCMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "opsworkscm"
    _SERVICE_PROP = "opsworkscm"
