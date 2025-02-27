"""
Wrapper for aioboto3 DataPipeline service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datapipeline/)

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
    # Returns type annotated aioboto3 DataPipeline client
    datapipeline_client = session.datapipeline.client()
    datapipeline_client: types_aiobotocore_datapipeline.client.DataPipelineClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_datapipeline.client import DataPipelineClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataPipelineService(ServiceFactory[DataPipelineClient]):
    SERVICE_NAME = "datapipeline"
    _SERVICE_PROP = "datapipeline"
