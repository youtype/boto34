"""
Wrapper for boto3 SagemakerEdgeManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_edge/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sagemaker_edge.client import SagemakerEdgeManagerClient

from boto34.boto3.service_factory import ServiceFactory


class SagemakerEdgeManagerService(ServiceFactory[SagemakerEdgeManagerClient]):
    """
    SagemakerEdgeManager service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_edge/)
    """
