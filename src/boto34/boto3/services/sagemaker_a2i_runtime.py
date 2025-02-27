"""
Wrapper for boto3 AugmentedAIRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_a2i_runtime/)

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
    # Returns type annotated boto3 AugmentedAIRuntime client
    sagemaker_a2i_runtime_client = session.sagemaker_a2i_runtime.client()
    sagemaker_a2i_runtime_client: types_boto3_sagemaker_a2i_runtime.client.AugmentedAIRuntimeClient
    ```
"""

from __future__ import annotations

from types_boto3_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class AugmentedAIRuntimeService(ServiceFactory[AugmentedAIRuntimeClient]):
    SERVICE_NAME = "sagemaker-a2i-runtime"
    _SERVICE_PROP = "sagemaker_a2i_runtime"
