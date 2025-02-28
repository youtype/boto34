"""
Wrapper for aioboto3 TelcoNetworkBuilder service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_tnb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_tnb.client import TelcoNetworkBuilderClient

from boto34.aioboto3.service_factory import ServiceFactory


class TelcoNetworkBuilderService(ServiceFactory[TelcoNetworkBuilderClient]):
    """
    TelcoNetworkBuilder service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_tnb/)
    """
