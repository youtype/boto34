"""
Wrapper for aiobotocore ConnectCampaignServiceV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcampaignsv2/)

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
    # Returns type annotated aiobotocore ConnectCampaignServiceV2 client
    async with session.connectcampaignsv2.create_client() as connectcampaignsv2_client:
        connectcampaignsv2_client: (
            types_aiobotocore_connectcampaignsv2.client.ConnectCampaignServiceV2Client
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_connectcampaignsv2.client import ConnectCampaignServiceV2Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_connectcampaignsv2.client import ConnectCampaignServiceV2Client
except ImportError:
    ConnectCampaignServiceV2Client = object  # type: ignore[misc,assignment]


class ConnectCampaignServiceV2Service(
    ServiceFactory[ConnectCampaignServiceV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connectcampaignsv2"
    _SERVICE_PROP = "connectcampaignsv2"
