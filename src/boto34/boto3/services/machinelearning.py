"""
Wrapper for boto3 MachineLearning service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_machinelearning/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_machinelearning.client import MachineLearningClient

from boto34.boto3.service_factory import ServiceFactory


class MachineLearningService(ServiceFactory[MachineLearningClient]):
    """
    MachineLearning service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_machinelearning/)
    """
