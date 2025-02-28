"""
Wrapper for aioboto3 Inspectorscan service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector_scan/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_inspector_scan.client import InspectorscanClient

from boto34.aioboto3.service_factory import ServiceFactory


class InspectorscanService(ServiceFactory[InspectorscanClient]):
    """
    Inspectorscan service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector_scan/)
    """
