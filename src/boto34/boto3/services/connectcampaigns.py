"""
Wrapper for boto3 ConnectCampaignService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectcampaigns/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ConnectCampaignService client
    connectcampaigns_client = session.connectcampaigns.client()
    connectcampaigns_client: types_boto3_connectcampaigns.client.ConnectCampaignServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_connectcampaigns.client import ConnectCampaignServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectCampaignServiceService(ServiceFactory[ConnectCampaignServiceClient]):
    SERVICE_NAME = "connectcampaigns"
    _SERVICE_PROP = "connectcampaigns"
