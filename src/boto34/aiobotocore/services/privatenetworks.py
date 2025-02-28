"""
Wrapper for aiobotocore Private5G service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_privatenetworks/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_privatenetworks.client import Private5GClient

from boto34.aiobotocore.service_factory import ServiceFactory


class Private5GService(ServiceFactory[Private5GClient]):
    """
    Private5G service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_privatenetworks/)
    """
