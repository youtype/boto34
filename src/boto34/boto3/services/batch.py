"""
Wrapper for boto3 Batch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_batch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Batch client
    batch_client = session.batch.client()
    batch_client: types_boto3_batch.client.BatchClient
    ```
"""

from __future__ import annotations

from types_boto3_batch.client import BatchClient

from boto34.boto3.service_factory import ServiceFactory


class BatchService(ServiceFactory[BatchClient]):
    SERVICE_NAME = "batch"
    _SERVICE_PROP = "batch"
