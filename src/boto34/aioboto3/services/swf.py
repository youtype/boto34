"""
Wrapper for aioboto3 SWF service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_swf/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_swf.client import SWFClient

from boto34.aioboto3.service_factory import ServiceFactory


class SWFService(ServiceFactory[SWFClient]):
    """
    SWF service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_swf/)
    """
