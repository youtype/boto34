"""
Wrapper for boto3 TaxSettings service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_taxsettings/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_taxsettings.client import TaxSettingsClient

from boto34.boto3.service_factory import ServiceFactory


class TaxSettingsService(ServiceFactory[TaxSettingsClient]):
    """
    TaxSettings service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_taxsettings/)
    """
