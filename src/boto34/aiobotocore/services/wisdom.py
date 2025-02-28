"""
Wrapper for aiobotocore ConnectWisdomService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wisdom/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_wisdom.client import ConnectWisdomServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectWisdomServiceService(ServiceFactory[ConnectWisdomServiceClient]):
    """
    ConnectWisdomService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wisdom/)
    """
