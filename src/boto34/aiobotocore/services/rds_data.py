"""
Wrapper for aiobotocore RDSDataService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rds_data/)

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
    # Returns type annotated aiobotocore RDSDataService client
    async with session.rds_data.create_client() as rds_data_client:
        rds_data_client: types_aiobotocore_rds_data.client.RDSDataServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_rds_data.client import RDSDataServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RDSDataServiceService(ServiceFactory[RDSDataServiceClient]):
    SERVICE_NAME = "rds-data"
    _SERVICE_PROP = "rds_data"
