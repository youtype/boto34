"""
Wrapper for aioboto3 GreengrassV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_greengrassv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_greengrassv2.client import GreengrassV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class GreengrassV2Service(ServiceFactory[GreengrassV2Client]):
    """
    GreengrassV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_greengrassv2/)
    """
