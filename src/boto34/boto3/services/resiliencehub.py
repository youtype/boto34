"""
Wrapper for boto3 ResilienceHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resiliencehub/)

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
    # Returns type annotated boto3 ResilienceHub client
    resiliencehub_client = session.resiliencehub.client()
    resiliencehub_client: types_boto3_resiliencehub.client.ResilienceHubClient
    ```
"""

from __future__ import annotations

from types_boto3_resiliencehub.client import ResilienceHubClient

from boto34.boto3.service_factory import ServiceFactory


class ResilienceHubService(ServiceFactory[ResilienceHubClient]):
    SERVICE_NAME = "resiliencehub"
    _SERVICE_PROP = "resiliencehub"
