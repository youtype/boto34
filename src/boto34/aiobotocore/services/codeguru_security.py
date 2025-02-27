"""
Wrapper for aiobotocore CodeGuruSecurity service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguru_security/)

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
    # Returns type annotated aiobotocore CodeGuruSecurity client
    async with session.codeguru_security.create_client() as codeguru_security_client:
        codeguru_security_client: types_aiobotocore_codeguru_security.client.CodeGuruSecurityClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codeguru_security.client import CodeGuruSecurityClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codeguru_security.client import CodeGuruSecurityClient
except ImportError:
    CodeGuruSecurityClient = object  # type: ignore[misc,assignment]


class CodeGuruSecurityService(
    ServiceFactory[CodeGuruSecurityClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeguru-security"
    _SERVICE_PROP = "codeguru_security"
