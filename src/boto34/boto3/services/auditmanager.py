"""
Wrapper for boto3 AuditManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_auditmanager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 AuditManager client
    auditmanager_client = session.auditmanager.client()
    auditmanager_client: types_boto3_auditmanager.client.AuditManagerClient
    ```
"""

from __future__ import annotations

from types_boto3_auditmanager.client import AuditManagerClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_auditmanager.client import AuditManagerClient
except ImportError:
    AuditManagerClient = object  # type: ignore[misc,assignment]


class AuditManagerService(
    ServiceFactory[AuditManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "auditmanager"
    _SERVICE_PROP = "auditmanager"
