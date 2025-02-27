"""
Wrapper for aiobotocore ACM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_acm/)

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
    # Returns type annotated aiobotocore ACM client
    async with session.acm.create_client() as acm_client:
        acm_client: types_aiobotocore_acm.client.ACMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_acm.client import ACMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ACMService(ServiceFactory[ACMClient]):
    SERVICE_NAME = "acm"
    _SERVICE_PROP = "acm"
