"""
Wrapper for aiobotocore ParallelComputingService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pcs/)

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
    # Returns type annotated aiobotocore ParallelComputingService client
    async with session.pcs.create_client() as pcs_client:
        pcs_client: types_aiobotocore_pcs.client.ParallelComputingServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pcs.client import ParallelComputingServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ParallelComputingServiceService(ServiceFactory[ParallelComputingServiceClient]):
    SERVICE_NAME = "pcs"
    _SERVICE_PROP = "pcs"
