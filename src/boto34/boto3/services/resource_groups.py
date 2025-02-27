"""
Wrapper for boto3 ResourceGroups service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resource_groups/)

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
    # Returns type annotated boto3 ResourceGroups client
    resource_groups_client = session.resource_groups.client()
    resource_groups_client: types_boto3_resource_groups.client.ResourceGroupsClient
    ```
"""

from __future__ import annotations

from types_boto3_resource_groups.client import ResourceGroupsClient

from boto34.boto3.service_factory import ServiceFactory


class ResourceGroupsService(ServiceFactory[ResourceGroupsClient]):
    SERVICE_NAME = "resource-groups"
    _SERVICE_PROP = "resource_groups"
