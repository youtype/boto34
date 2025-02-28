"""
Wrapper for boto3 SSOAdmin service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso_admin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sso_admin.client import SSOAdminClient

from boto34.boto3.service_factory import ServiceFactory


class SSOAdminService(ServiceFactory[SSOAdminClient]):
    """
    SSOAdmin service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso_admin/)
    """
