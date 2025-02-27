"""
Wrapper for aioboto3 CodeGuruSecurity service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeguru_security/)

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
    # Returns type annotated aioboto3 CodeGuruSecurity client
    codeguru_security_client = session.codeguru_security.client()
    codeguru_security_client: types_aiobotocore_codeguru_security.client.CodeGuruSecurityClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_codeguru_security.client import CodeGuruSecurityClient
except ImportError:
    CodeGuruSecurityClient = object  # type: ignore[misc,assignment]


class CodeGuruSecurityService(
    ServiceFactory[CodeGuruSecurityClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeguru-security"
    _SERVICE_PROP = "codeguru_security"
