"""
Wrapper for aiobotocore STS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sts.client import STSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class STSService(ServiceFactory[STSClient]):
    """
    STS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sts/)
    """
