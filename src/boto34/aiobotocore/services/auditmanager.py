"""
Wrapper for aiobotocore AuditManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_auditmanager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore AuditManager client
    async with session.auditmanager.create_client() as auditmanager_client:
        auditmanager_client: types_aiobotocore_auditmanager.client.AuditManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_auditmanager.client import AuditManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AuditManagerService(ServiceFactory[AuditManagerClient]):
    SERVICE_NAME = "auditmanager"
    _SERVICE_PROP = "auditmanager"
