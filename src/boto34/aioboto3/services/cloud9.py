"""
Wrapper for aioboto3 Cloud9 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloud9/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloud9.client import Cloud9Client

from boto34.aioboto3.service_factory import ServiceFactory


class Cloud9Service(ServiceFactory[Cloud9Client]):
    """
    Cloud9 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloud9/)
    """
