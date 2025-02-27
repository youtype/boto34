"""
Wrapper for aioboto3 ParallelComputingService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pcs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ParallelComputingService client
    pcs_client = session.pcs.client()
    pcs_client: types_aiobotocore_pcs.client.ParallelComputingServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pcs.client import ParallelComputingServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ParallelComputingServiceService(ServiceFactory[ParallelComputingServiceClient]):
    SERVICE_NAME = "pcs"
    _SERVICE_PROP = "pcs"
