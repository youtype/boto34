"""
Wrapper for boto3 SageMakerMetrics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_metrics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sagemaker_metrics.client import SageMakerMetricsClient

from boto34.boto3.service_factory import ServiceFactory


class SageMakerMetricsService(ServiceFactory[SageMakerMetricsClient]):
    """
    SageMakerMetrics service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_metrics/)
    """
