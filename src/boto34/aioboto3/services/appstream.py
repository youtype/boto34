"""
Wrapper for aioboto3 AppStream service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appstream/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appstream.client import AppStreamClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppStreamService(ServiceFactory[AppStreamClient]):
    """
    AppStream service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appstream/)
    """
