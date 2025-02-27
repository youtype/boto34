"""
Wrapper for boto3 TaxSettings service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_taxsettings/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 TaxSettings client
    taxsettings_client = session.taxsettings.client()
    taxsettings_client: types_boto3_taxsettings.client.TaxSettingsClient
    ```
"""

from __future__ import annotations

from types_boto3_taxsettings.client import TaxSettingsClient

from boto34.boto3.service_factory import ServiceFactory


class TaxSettingsService(ServiceFactory[TaxSettingsClient]):
    SERVICE_NAME = "taxsettings"
    _SERVICE_PROP = "taxsettings"
