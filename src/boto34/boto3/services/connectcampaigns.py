"""
Wrapper for boto3 ConnectCampaignService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectcampaigns/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_connectcampaigns.client import ConnectCampaignServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectCampaignServiceService(ServiceFactory[ConnectCampaignServiceClient]):
    """
    ConnectCampaignService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectcampaigns/)
    """
