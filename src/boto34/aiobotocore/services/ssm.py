"""
Wrapper for aiobotocore SSM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm/)

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
    # Returns type annotated aiobotocore SSM client
    async with session.ssm.create_client() as ssm_client:
        ssm_client: types_aiobotocore_ssm.client.SSMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ssm.client import SSMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSMService(ServiceFactory[SSMClient]):
    SERVICE_NAME = "ssm"
    _SERVICE_PROP = "ssm"
