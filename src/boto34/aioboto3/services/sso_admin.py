"""
Wrapper for aioboto3 SSOAdmin service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sso_admin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sso_admin.client import SSOAdminClient

from boto34.aioboto3.service_factory import ServiceFactory


class SSOAdminService(ServiceFactory[SSOAdminClient]):
    """
    SSOAdmin service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sso_admin/)
    """
