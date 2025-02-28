"""
Wrapper for aioboto3 MachineLearning service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_machinelearning/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_machinelearning.client import MachineLearningClient

from boto34.aioboto3.service_factory import ServiceFactory


class MachineLearningService(ServiceFactory[MachineLearningClient]):
    """
    MachineLearning service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_machinelearning/)
    """
