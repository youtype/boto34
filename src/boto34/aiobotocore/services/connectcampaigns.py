"""
Wrapper for aiobotocore ConnectCampaignService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcampaigns/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_connectcampaigns.client import ConnectCampaignServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectCampaignServiceService(ServiceFactory[ConnectCampaignServiceClient]):
    """
    ConnectCampaignService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcampaigns/)
    """
