"""
Wrapper for aioboto3 XRay service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_xray/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_xray.client import XRayClient

from boto34.aioboto3.service_factory import ServiceFactory


class XRayService(ServiceFactory[XRayClient]):
    """
    XRay service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_xray/)
    """
