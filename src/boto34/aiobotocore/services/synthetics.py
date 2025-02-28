"""
Wrapper for aiobotocore Synthetics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_synthetics.client import SyntheticsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SyntheticsService(ServiceFactory[SyntheticsClient]):
    """
    Synthetics service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/)
    """
