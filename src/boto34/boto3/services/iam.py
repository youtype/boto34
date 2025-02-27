"""
Wrapper for boto3 IAM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iam/)

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
    # Returns type annotated boto3 IAM client
    iam_client = session.iam.client()
    iam_client: types_boto3_iam.client.IAMClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 IAM resource
    iam_resource = session.iam.resource()
    iam_resource: types_boto3_iam.service_resource.IAMServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_iam.client import IAMClient

from boto34.boto3.service_factory import ServiceResourceFactory

try:
    from types_boto3_iam.client import IAMClient
    from types_boto3_iam.service_resource import IAMServiceResource
except ImportError:
    IAMClient = object  # type: ignore[misc,assignment]
    IAMServiceResource = object  # type: ignore[misc,assignment]


class IAMService(
    ServiceResourceFactory[IAMClient, IAMServiceResource]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iam"
    _SERVICE_PROP = "iam"
