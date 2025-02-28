"""
Wrapper for aioboto3 ACM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_acm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_acm.client import ACMClient

from boto34.aioboto3.service_factory import ServiceFactory


class ACMService(ServiceFactory[ACMClient]):
    """
    ACM service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_acm/)
    """
