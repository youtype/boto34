"""
Wrapper for aioboto3 Lightsail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lightsail/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lightsail.client import LightsailClient

from boto34.aioboto3.service_factory import ServiceFactory


class LightsailService(ServiceFactory[LightsailClient]):
    """
    Lightsail service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lightsail/)
    """
