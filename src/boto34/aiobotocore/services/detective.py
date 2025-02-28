"""
Wrapper for aiobotocore Detective service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_detective/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_detective.client import DetectiveClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DetectiveService(ServiceFactory[DetectiveClient]):
    """
    Detective service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_detective/)
    """
