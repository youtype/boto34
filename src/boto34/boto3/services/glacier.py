"""
Wrapper for boto3 Glacier service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_glacier/)

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
    # Returns type annotated boto3 Glacier client
    glacier_client = session.glacier.client()
    glacier_client: types_boto3_glacier.client.GlacierClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 Glacier resource
    glacier_resource = session.glacier.resource()
    glacier_resource: types_boto3_glacier.service_resource.GlacierServiceResource
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceResourceFactory

try:
    from types_boto3_glacier.client import GlacierClient
    from types_boto3_glacier.service_resource import GlacierServiceResource
except ImportError:
    GlacierClient = object  # type: ignore[misc,assignment]
    GlacierServiceResource = object  # type: ignore[misc,assignment]


class GlacierService(
    ServiceResourceFactory[GlacierClient, GlacierServiceResource]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "glacier"
    _SERVICE_PROP = "glacier"
