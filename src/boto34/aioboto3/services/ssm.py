"""
Wrapper for aioboto3 SSM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm.client import SSMClient

from boto34.aioboto3.service_factory import ServiceFactory


class SSMService(ServiceFactory[SSMClient]):
    """
    SSM service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm/)
    """
