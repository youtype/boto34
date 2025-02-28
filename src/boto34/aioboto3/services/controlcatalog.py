"""
Wrapper for aioboto3 ControlCatalog service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_controlcatalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_controlcatalog.client import ControlCatalogClient

from boto34.aioboto3.service_factory import ServiceFactory


class ControlCatalogService(ServiceFactory[ControlCatalogClient]):
    """
    ControlCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_controlcatalog/)
    """
