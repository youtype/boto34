"""
Wrapper for aiobotocore IAM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iam/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iam.client import IAMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IAMService(ServiceFactory[IAMClient]):
    """
    IAM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iam/)
    """
