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

    # Type annotated shortcuts for boto3.Client.get_waiter
    # Initialize client first to use it

    s3_waiter = session.s3.get_waiters(s3_client).bucket_exists
    s3_waiter: types_boto3_s3.waiter.BucketExistsWaiter

    # Type annotated shortcuts for boto3.Client.get_paginator
    # Initialize client first to use it

    s3_paginator = session.s3.get_paginators(s3_client).list_buckets
    s3_paginator: types_boto3_s3.paginator.ListBucketsPaginator```
"""

from __future__ import annotations

from types_boto3_s3.client import S3Client
from types_boto3_s3.paginator import (
    ListBucketsPaginator,
    ListDirectoryBucketsPaginator,
    ListMultipartUploadsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListObjectVersionsPaginator,
    ListPartsPaginator,
)
from types_boto3_s3.service_resource import S3ServiceResource
from types_boto3_s3.waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)

from boto34.boto3.client_factory import ClientFactory
from boto34.boto3.service_factory import ServiceResourceFactory


class S3WaiterFactory(ClientFactory[S3Client]):
    @property
    def bucket_exists(self) -> BucketExistsWaiter:
        return self._client.get_waiter("bucket_exists")

    @property
    def bucket_not_exists(self) -> BucketNotExistsWaiter:
        return self._client.get_waiter("bucket_not_exists")

    @property
    def object_exists(self) -> ObjectExistsWaiter:
        return self._client.get_waiter("object_exists")

    @property
    def object_not_exists(self) -> ObjectNotExistsWaiter:
        return self._client.get_waiter("object_not_exists")


class S3PaginatorFactory(ClientFactory[S3Client]):
    @property
    def list_buckets(self) -> ListBucketsPaginator:
        return self._client.get_paginator("list_buckets")

    @property
    def list_directory_buckets(self) -> ListDirectoryBucketsPaginator:
        return self._client.get_paginator("list_directory_buckets")

    @property
    def list_multipart_uploads(self) -> ListMultipartUploadsPaginator:
        return self._client.get_paginator("list_multipart_uploads")

    @property
    def list_object_versions(self) -> ListObjectVersionsPaginator:
        return self._client.get_paginator("list_object_versions")

    @property
    def list_objects(self) -> ListObjectsPaginator:
        return self._client.get_paginator("list_objects")

    @property
    def list_objects_v2(self) -> ListObjectsV2Paginator:
        return self._client.get_paginator("list_objects_v2")

    @property
    def list_parts(self) -> ListPartsPaginator:
        return self._client.get_paginator("list_parts")


class S3Service(
    ServiceResourceFactory[
        S3Client,
        S3ServiceResource,
        S3WaiterFactory,
        S3PaginatorFactory,
    ]
):
    SERVICE_NAME = "s3"
    _SERVICE_PROP = "s3"
    _WAITER_FACTORY_CLS = S3WaiterFactory
    _PAGINATOR_FACTORY_CLS = S3PaginatorFactory

    def get_waiters(self, client: S3Client) -> S3WaiterFactory:
        return self._get_waiter_factory(client)

    def get_paginators(self, client: S3Client) -> S3PaginatorFactory:
        return self._get_paginator_factory(client)
