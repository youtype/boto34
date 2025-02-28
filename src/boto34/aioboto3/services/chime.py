"""
Wrapper for aioboto3 Chime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_chime.client import ChimeClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChimeService(ServiceFactory[ChimeClient]):
    """
    Chime service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime/)
    """
