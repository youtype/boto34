"""
Wrapper for aioboto3 PartnerCentralSellingAPI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_partnercentral_selling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_partnercentral_selling.client import PartnerCentralSellingAPIClient

from boto34.aioboto3.service_factory import ServiceFactory


class PartnerCentralSellingAPIService(ServiceFactory[PartnerCentralSellingAPIClient]):
    """
    PartnerCentralSellingAPI service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_partnercentral_selling/)
    """
