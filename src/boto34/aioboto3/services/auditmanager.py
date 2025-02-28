"""
Wrapper for aioboto3 AuditManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_auditmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_auditmanager.client import AuditManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class AuditManagerService(ServiceFactory[AuditManagerClient]):
    """
    AuditManager service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_auditmanager/)
    """
