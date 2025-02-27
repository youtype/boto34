"""
Wrapper for aioboto3 ConnectCampaignService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connectcampaigns/)

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
    # Returns type annotated aioboto3 ConnectCampaignService client
    connectcampaigns_client = session.connectcampaigns.client()
    connectcampaigns_client: types_aiobotocore_connectcampaigns.client.ConnectCampaignServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_connectcampaigns.client import ConnectCampaignServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ConnectCampaignServiceService(ServiceFactory[ConnectCampaignServiceClient]):
    SERVICE_NAME = "connectcampaigns"
    _SERVICE_PROP = "connectcampaigns"
