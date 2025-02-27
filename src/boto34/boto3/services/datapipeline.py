"""
Wrapper for boto3 DataPipeline service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datapipeline/)

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
    # Returns type annotated boto3 DataPipeline client
    datapipeline_client = session.datapipeline.client()
    datapipeline_client: types_boto3_datapipeline.client.DataPipelineClient
    ```
"""

from __future__ import annotations

from types_boto3_datapipeline.client import DataPipelineClient

from boto34.boto3.service_factory import ServiceFactory


class DataPipelineService(ServiceFactory[DataPipelineClient]):
    SERVICE_NAME = "datapipeline"
    _SERVICE_PROP = "datapipeline"
