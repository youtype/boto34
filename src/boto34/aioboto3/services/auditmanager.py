"""
Wrapper for aioboto3 AuditManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_auditmanager/)

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
    # Returns type annotated aioboto3 AuditManager client
    auditmanager_client = session.auditmanager.client()
    auditmanager_client: types_aiobotocore_auditmanager.client.AuditManagerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_auditmanager.client import AuditManagerClient
except ImportError:
    AuditManagerClient = object  # type: ignore[misc,assignment]


class AuditManagerService(
    ServiceFactory[AuditManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "auditmanager"
    _SERVICE_PROP = "auditmanager"
