"""
Wrapper for aiobotocore TaxSettings service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_taxsettings/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore TaxSettings client
    async with session.taxsettings.create_client() as taxsettings_client:
        taxsettings_client: types_aiobotocore_taxsettings.client.TaxSettingsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_taxsettings.client import TaxSettingsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TaxSettingsService(ServiceFactory[TaxSettingsClient]):
    SERVICE_NAME = "taxsettings"
    _SERVICE_PROP = "taxsettings"
