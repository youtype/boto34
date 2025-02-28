"""
Wrapper for aioboto3 Shield service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_shield/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_shield.client import ShieldClient

from boto34.aioboto3.service_factory import ServiceFactory


class ShieldService(ServiceFactory[ShieldClient]):
    """
    Shield service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_shield/)
    """
