"""
Wrapper for boto3 PartnerCentralSellingAPI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_partnercentral_selling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_partnercentral_selling.client import PartnerCentralSellingAPIClient

from boto34.boto3.service_factory import ServiceFactory


class PartnerCentralSellingAPIService(ServiceFactory[PartnerCentralSellingAPIClient]):
    """
    PartnerCentralSellingAPI service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_partnercentral_selling/)
    """
