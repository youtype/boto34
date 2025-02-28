"""
Wrapper for boto3 AuditManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_auditmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_auditmanager.client import AuditManagerClient

from boto34.boto3.service_factory import ServiceFactory


class AuditManagerService(ServiceFactory[AuditManagerClient]):
    """
    AuditManager service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_auditmanager/)
    """
