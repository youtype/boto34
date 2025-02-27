"""
Wrapper for aioboto3 SecurityIncidentResponse service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_security_ir/)

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
    # Returns type annotated aioboto3 SecurityIncidentResponse client
    security_ir_client = session.security_ir.client()
    security_ir_client: types_aiobotocore_security_ir.client.SecurityIncidentResponseClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_security_ir.client import SecurityIncidentResponseClient

from boto34.aioboto3.service_factory import ServiceFactory


class SecurityIncidentResponseService(ServiceFactory[SecurityIncidentResponseClient]):
    SERVICE_NAME = "security-ir"
    _SERVICE_PROP = "security_ir"
