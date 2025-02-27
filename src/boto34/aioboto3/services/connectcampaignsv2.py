"""
Wrapper for aioboto3 ConnectCampaignServiceV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connectcampaignsv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ConnectCampaignServiceV2 client
    connectcampaignsv2_client = session.connectcampaignsv2.client()
    connectcampaignsv2_client: (
        types_aiobotocore_connectcampaignsv2.client.ConnectCampaignServiceV2Client
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_connectcampaignsv2.client import ConnectCampaignServiceV2Client
except ImportError:
    ConnectCampaignServiceV2Client = object  # type: ignore[misc,assignment]


class ConnectCampaignServiceV2Service(
    ServiceFactory[ConnectCampaignServiceV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connectcampaignsv2"
    _SERVICE_PROP = "connectcampaignsv2"
