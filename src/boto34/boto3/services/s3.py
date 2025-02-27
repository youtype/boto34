"""
Wrapper for boto3 S3 1.37.1 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3/)

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
    # Returns type annotated boto3 S3 client
    s3_client = session.s3.client()
    s3_client: types_boto3_s3.client.S3Client

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 S3 resource
    s3_resource = session.s3.resource()
    s3_resource: types_boto3_s3.service_resource.S3ServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_s3.client import S3Client

from boto34.boto3.service_factory import ServiceResourceFactory

try:
    from types_boto3_s3.client import S3Client
    from types_boto3_s3.service_resource import S3ServiceResource
except ImportError:
    S3Client = object  # type: ignore[misc,assignment]
    S3ServiceResource = object  # type: ignore[misc,assignment]


class S3Service(
    ServiceResourceFactory[S3Client, S3ServiceResource]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "s3"
    _SERVICE_PROP = "s3"
