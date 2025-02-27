"""
Wrapper for boto3 ResourceGroupsTaggingAPI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/)

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
    # Returns type annotated boto3 ResourceGroupsTaggingAPI client
    resourcegroupstaggingapi_client = session.resourcegroupstaggingapi.client()
    resourcegroupstaggingapi_client: (
        types_boto3_resourcegroupstaggingapi.client.ResourceGroupsTaggingAPIClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient
except ImportError:
    ResourceGroupsTaggingAPIClient = object  # type: ignore[misc,assignment]


class ResourceGroupsTaggingAPIService(
    ServiceFactory[ResourceGroupsTaggingAPIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "resourcegroupstaggingapi"
    _SERVICE_PROP = "resourcegroupstaggingapi"
