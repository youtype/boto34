"""
Wrapper for aioboto3 PinpointEmail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint_email/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pinpoint_email.client import PinpointEmailClient

from boto34.aioboto3.service_factory import ServiceFactory


class PinpointEmailService(ServiceFactory[PinpointEmailClient]):
    """
    PinpointEmail service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pinpoint_email/)
    """
