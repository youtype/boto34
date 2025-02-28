"""
Wrapper for aioboto3 PI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pi.client import PIClient

from boto34.aioboto3.service_factory import ServiceFactory


class PIService(ServiceFactory[PIClient]):
    """
    PI service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pi/)
    """
