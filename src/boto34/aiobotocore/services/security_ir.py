"""
Wrapper for aiobotocore SecurityIncidentResponse service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_security_ir/)

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
    # Returns type annotated aiobotocore SecurityIncidentResponse client
    async with session.security_ir.create_client() as security_ir_client:
        security_ir_client: types_aiobotocore_security_ir.client.SecurityIncidentResponseClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_security_ir.client import SecurityIncidentResponseClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SecurityIncidentResponseService(ServiceFactory[SecurityIncidentResponseClient]):
    SERVICE_NAME = "security-ir"
    _SERVICE_PROP = "security_ir"
