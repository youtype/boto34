"""
Wrapper for aiobotocore ECR service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecr/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ecr.client import ECRClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ECRService(ServiceFactory[ECRClient]):
    """
    ECR service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecr/)
    """
