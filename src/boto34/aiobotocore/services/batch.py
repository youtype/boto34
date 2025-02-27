"""
Wrapper for aiobotocore Batch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_batch/)

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
    # Returns type annotated aiobotocore Batch client
    async with session.batch.create_client() as batch_client:
        batch_client: types_aiobotocore_batch.client.BatchClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_batch.client import BatchClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_batch.client import BatchClient
except ImportError:
    BatchClient = object  # type: ignore[misc,assignment]


class BatchService(
    ServiceFactory[BatchClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "batch"
    _SERVICE_PROP = "batch"
