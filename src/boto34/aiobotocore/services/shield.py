"""
Wrapper for aiobotocore Shield service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_shield/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_shield.client import ShieldClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ShieldService(ServiceFactory[ShieldClient]):
    """
    Shield service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_shield/)
    """
