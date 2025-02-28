"""
Wrapper for aioboto3 SESV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sesv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sesv2.client import SESV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class SESV2Service(ServiceFactory[SESV2Client]):
    """
    SESV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sesv2/)
    """
