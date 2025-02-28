"""
Wrapper for aiobotocore TaxSettings service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_taxsettings/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_taxsettings.client import TaxSettingsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TaxSettingsService(ServiceFactory[TaxSettingsClient]):
    """
    TaxSettings service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_taxsettings/)
    """
