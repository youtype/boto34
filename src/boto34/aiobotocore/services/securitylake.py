"""
Wrapper for aiobotocore SecurityLake service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securitylake/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_securitylake.client import SecurityLakeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SecurityLakeService(ServiceFactory[SecurityLakeClient]):
    """
    SecurityLake service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securitylake/)
    """
