"""
Wrapper for aiobotocore EBS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ebs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ebs.client import EBSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EBSService(ServiceFactory[EBSClient]):
    """
    EBS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ebs/)
    """
