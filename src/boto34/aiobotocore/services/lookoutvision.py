"""
Wrapper for aiobotocore LookoutforVision service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutvision/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lookoutvision.client import LookoutforVisionClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LookoutforVisionService(ServiceFactory[LookoutforVisionClient]):
    """
    LookoutforVision service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutvision/)
    """
