"""
Wrapper for aiobotocore SSM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm.client import SSMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSMService(ServiceFactory[SSMClient]):
    """
    SSM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm/)
    """
