"""
Wrapper for aioboto3 IAM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iam/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iam.client import IAMClient
from types_aiobotocore_iam.service_resource import IAMServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class IAMService(ServiceResourceFactory[IAMClient, IAMServiceResource]):
    """
    IAM service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iam/)
    """
