"""
Wrapper for boto3 SageMaker service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker/)

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
    # Returns type annotated boto3 SageMaker client
    sagemaker_client = session.sagemaker.client()
    sagemaker_client: types_boto3_sagemaker.client.SageMakerClient
    ```
"""

from __future__ import annotations

from types_boto3_sagemaker.client import SageMakerClient

from boto34.boto3.service_factory import ServiceFactory


class SageMakerService(ServiceFactory[SageMakerClient]):
    SERVICE_NAME = "sagemaker"
    _SERVICE_PROP = "sagemaker"
