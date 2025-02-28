"""
Wrapper for aiobotocore MachineLearning service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_machinelearning/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_machinelearning.client import MachineLearningClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MachineLearningService(ServiceFactory[MachineLearningClient]):
    """
    MachineLearning service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_machinelearning/)
    """
