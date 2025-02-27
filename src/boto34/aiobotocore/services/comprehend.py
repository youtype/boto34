"""
Wrapper for aiobotocore Comprehend service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/)

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
    # Returns type annotated aiobotocore Comprehend client
    async with session.comprehend.create_client() as comprehend_client:
        comprehend_client: types_aiobotocore_comprehend.client.ComprehendClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_comprehend.client import ComprehendClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ComprehendService(ServiceFactory[ComprehendClient]):
    SERVICE_NAME = "comprehend"
    _SERVICE_PROP = "comprehend"
