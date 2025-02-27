"""
Wrapper for aiobotocore RDS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rds/)

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
    # Returns type annotated aiobotocore RDS client
    async with session.rds.create_client() as rds_client:
        rds_client: types_aiobotocore_rds.client.RDSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_rds.client import RDSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RDSService(ServiceFactory[RDSClient]):
    SERVICE_NAME = "rds"
    _SERVICE_PROP = "rds"
