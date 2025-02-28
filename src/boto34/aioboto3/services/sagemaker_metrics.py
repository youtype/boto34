"""
Wrapper for aioboto3 SageMakerMetrics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_metrics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_metrics.client import SageMakerMetricsClient

from boto34.aioboto3.service_factory import ServiceFactory


class SageMakerMetricsService(ServiceFactory[SageMakerMetricsClient]):
    """
    SageMakerMetrics service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_metrics/)
    """
