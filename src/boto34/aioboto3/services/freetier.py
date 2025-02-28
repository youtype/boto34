"""
Wrapper for aioboto3 FreeTier service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_freetier/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_freetier.client import FreeTierClient

from boto34.aioboto3.service_factory import ServiceFactory


class FreeTierService(ServiceFactory[FreeTierClient]):
    """
    FreeTier service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_freetier/)
    """
