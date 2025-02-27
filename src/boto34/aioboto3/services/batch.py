"""
Wrapper for aioboto3 Batch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_batch/)

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
    # Returns type annotated aioboto3 Batch client
    batch_client = session.batch.client()
    batch_client: types_aiobotocore_batch.client.BatchClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_batch.client import BatchClient

from boto34.aioboto3.service_factory import ServiceFactory


class BatchService(ServiceFactory[BatchClient]):
    SERVICE_NAME = "batch"
    _SERVICE_PROP = "batch"
