"""
Wrapper for aioboto3 DataPipeline service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datapipeline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_datapipeline.client import DataPipelineClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataPipelineService(ServiceFactory[DataPipelineClient]):
    """
    DataPipeline service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datapipeline/)
    """
