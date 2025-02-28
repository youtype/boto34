"""
Wrapper for aioboto3 GroundStation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_groundstation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_groundstation.client import GroundStationClient

from boto34.aioboto3.service_factory import ServiceFactory


class GroundStationService(ServiceFactory[GroundStationClient]):
    """
    GroundStation service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_groundstation/)
    """
