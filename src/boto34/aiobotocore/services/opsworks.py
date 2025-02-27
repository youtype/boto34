"""
Wrapper for aiobotocore OpsWorks service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/)

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
    # Returns type annotated aiobotocore OpsWorks client
    async with session.opsworks.create_client() as opsworks_client:
        opsworks_client: types_aiobotocore_opsworks.client.OpsWorksClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_opsworks.client import OpsWorksClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpsWorksService(ServiceFactory[OpsWorksClient]):
    SERVICE_NAME = "opsworks"
    _SERVICE_PROP = "opsworks"
