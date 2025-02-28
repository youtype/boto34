"""
Wrapper for aioboto3 TaxSettings service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_taxsettings/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_taxsettings.client import TaxSettingsClient

from boto34.aioboto3.service_factory import ServiceFactory


class TaxSettingsService(ServiceFactory[TaxSettingsClient]):
    """
    TaxSettings service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_taxsettings/)
    """
