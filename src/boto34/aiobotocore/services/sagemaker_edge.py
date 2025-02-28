"""
Wrapper for aiobotocore SagemakerEdgeManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_edge/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_edge.client import SagemakerEdgeManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SagemakerEdgeManagerService(ServiceFactory[SagemakerEdgeManagerClient]):
    """
    SagemakerEdgeManager service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_edge/)
    """
