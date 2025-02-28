"""
Wrapper for aioboto3 ECRPublic service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecr_public/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ecr_public.client import ECRPublicClient

from boto34.aioboto3.service_factory import ServiceFactory


class ECRPublicService(ServiceFactory[ECRPublicClient]):
    """
    ECRPublic service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecr_public/)
    """
