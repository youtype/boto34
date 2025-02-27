"""
Wrapper for boto3 SecurityIncidentResponse service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_security_ir/)

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
    # Returns type annotated boto3 SecurityIncidentResponse client
    security_ir_client = session.security_ir.client()
    security_ir_client: types_boto3_security_ir.client.SecurityIncidentResponseClient
    ```
"""

from __future__ import annotations

from types_boto3_security_ir.client import SecurityIncidentResponseClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_security_ir.client import SecurityIncidentResponseClient
except ImportError:
    SecurityIncidentResponseClient = object  # type: ignore[misc,assignment]


class SecurityIncidentResponseService(
    ServiceFactory[SecurityIncidentResponseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "security-ir"
    _SERVICE_PROP = "security_ir"
