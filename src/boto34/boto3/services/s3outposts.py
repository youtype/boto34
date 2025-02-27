"""
Wrapper for boto3 S3Outposts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3outposts/)

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
    # Returns type annotated boto3 S3Outposts client
    s3outposts_client = session.s3outposts.client()
    s3outposts_client: types_boto3_s3outposts.client.S3OutpostsClient
    ```
"""

from __future__ import annotations

from types_boto3_s3outposts.client import S3OutpostsClient

from boto34.boto3.service_factory import ServiceFactory


class S3OutpostsService(ServiceFactory[S3OutpostsClient]):
    SERVICE_NAME = "s3outposts"
    _SERVICE_PROP = "s3outposts"
