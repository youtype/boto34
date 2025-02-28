"""
Wrapper for aioboto3 Pinpoint service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pinpoint.client import PinpointClient

from boto34.aioboto3.service_factory import ServiceFactory


class PinpointService(ServiceFactory[PinpointClient]):
    """
    Pinpoint service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint/)
    """
