"""
Wrapper for boto3 DataPipeline service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datapipeline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_datapipeline.client import DataPipelineClient

from boto34.boto3.service_factory import ServiceFactory


class DataPipelineService(ServiceFactory[DataPipelineClient]):
    """
    DataPipeline service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datapipeline/)
    """
