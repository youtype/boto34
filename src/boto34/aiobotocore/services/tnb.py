"""
Wrapper for aiobotocore TelcoNetworkBuilder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_tnb.client import TelcoNetworkBuilderClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TelcoNetworkBuilderService(ServiceFactory[TelcoNetworkBuilderClient]):
    """
    TelcoNetworkBuilder service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/)
    """
