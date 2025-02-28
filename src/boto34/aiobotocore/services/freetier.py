"""
Wrapper for aiobotocore FreeTier service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_freetier/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_freetier.client import FreeTierClient

from boto34.aiobotocore.service_factory import ServiceFactory


class FreeTierService(ServiceFactory[FreeTierClient]):
    """
    FreeTier service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_freetier/)
    """
