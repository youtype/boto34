"""
Wrapper for aiobotocore DataPipeline service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datapipeline/)

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
    # Returns type annotated aiobotocore DataPipeline client
    async with session.datapipeline.create_client() as datapipeline_client:
        datapipeline_client: types_aiobotocore_datapipeline.client.DataPipelineClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_datapipeline.client import DataPipelineClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DataPipelineService(ServiceFactory[DataPipelineClient]):
    SERVICE_NAME = "datapipeline"
    _SERVICE_PROP = "datapipeline"
