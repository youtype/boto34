"""
Wrapper for aiobotocore CloudHSM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudhsm/)

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
    # Returns type annotated aiobotocore CloudHSM client
    async with session.cloudhsm.create_client() as cloudhsm_client:
        cloudhsm_client: types_aiobotocore_cloudhsm.client.CloudHSMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudhsm.client import CloudHSMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudHSMService(ServiceFactory[CloudHSMClient]):
    SERVICE_NAME = "cloudhsm"
    _SERVICE_PROP = "cloudhsm"
