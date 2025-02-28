"""
Wrapper for boto3 AppStream service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appstream/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_appstream.client import AppStreamClient

from boto34.boto3.service_factory import ServiceFactory


class AppStreamService(ServiceFactory[AppStreamClient]):
    """
    AppStream service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appstream/)
    """
