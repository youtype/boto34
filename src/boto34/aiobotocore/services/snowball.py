"""
Wrapper for aiobotocore Snowball service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_snowball/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_snowball.client import SnowballClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SnowballService(ServiceFactory[SnowballClient]):
    """
    Snowball service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_snowball/)
    """
