"""
Wrapper for aiobotocore ConnectCampaignServiceV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcampaignsv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_connectcampaignsv2.client import ConnectCampaignServiceV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectCampaignServiceV2Service(ServiceFactory[ConnectCampaignServiceV2Client]):
    """
    ConnectCampaignServiceV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcampaignsv2/)
    """
