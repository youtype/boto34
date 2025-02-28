"""
Wrapper for aiobotocore FMS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_fms.client import FMSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class FMSService(ServiceFactory[FMSClient]):
    """
    FMS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fms/)
    """
