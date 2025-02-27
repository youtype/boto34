"""
Wrapper for aioboto3 S3 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_s3/)

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
    # Returns type annotated aioboto3 S3 client
    s3_client = session.s3.client()
    s3_client: types_aiobotocore_s3.client.S3Client

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 S3 resource
    s3_resource = session.s3.resource()
    s3_resource: types_aiobotocore_s3.service_resource.S3ServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_s3.client import S3Client
from types_aiobotocore_s3.service_resource import S3ServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class S3Service(ServiceResourceFactory[S3Client, S3ServiceResource]):
    SERVICE_NAME = "s3"
    _SERVICE_PROP = "s3"
