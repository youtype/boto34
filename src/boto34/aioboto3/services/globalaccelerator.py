"""
Wrapper for aioboto3 GlobalAccelerator service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_globalaccelerator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_globalaccelerator.client import GlobalAcceleratorClient

from boto34.aioboto3.service_factory import ServiceFactory


class GlobalAcceleratorService(ServiceFactory[GlobalAcceleratorClient]):
    """
    GlobalAccelerator service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_globalaccelerator/)
    """
