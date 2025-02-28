"""
Wrapper for aiobotocore DataPipeline service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datapipeline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_datapipeline.client import DataPipelineClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DataPipelineService(ServiceFactory[DataPipelineClient]):
    """
    DataPipeline service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datapipeline/)
    """
