"""
Wrapper for aiobotocore ConnectCampaignService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcampaigns/)

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
    # Returns type annotated aiobotocore ConnectCampaignService client
    async with session.connectcampaigns.create_client() as connectcampaigns_client:
        connectcampaigns_client: types_aiobotocore_connectcampaigns.client.ConnectCampaignServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_connectcampaigns.client import ConnectCampaignServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectCampaignServiceService(ServiceFactory[ConnectCampaignServiceClient]):
    SERVICE_NAME = "connectcampaigns"
    _SERVICE_PROP = "connectcampaigns"
