"""
Wrapper for aiobotocore ControlCatalog service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controlcatalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_controlcatalog.client import ControlCatalogClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ControlCatalogService(ServiceFactory[ControlCatalogClient]):
    """
    ControlCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controlcatalog/)
    """
