"""
Wrapper for aiobotocore SSO service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso/)

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
    # Returns type annotated aiobotocore SSO client
    async with session.sso.create_client() as sso_client:
        sso_client: types_aiobotocore_sso.client.SSOClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sso.client import SSOClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSOService(ServiceFactory[SSOClient]):
    SERVICE_NAME = "sso"
    _SERVICE_PROP = "sso"
