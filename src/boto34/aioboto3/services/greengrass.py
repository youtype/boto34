"""
Wrapper for aioboto3 Greengrass service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_greengrass/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_greengrass.client import GreengrassClient

from boto34.aioboto3.service_factory import ServiceFactory


class GreengrassService(ServiceFactory[GreengrassClient]):
    """
    Greengrass service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_greengrass/)
    """
