"""
Wrapper for aioboto3 STS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sts.client import STSClient

from boto34.aioboto3.service_factory import ServiceFactory


class STSService(ServiceFactory[STSClient]):
    """
    STS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sts/)
    """
