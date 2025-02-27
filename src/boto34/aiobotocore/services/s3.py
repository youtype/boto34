"""
Wrapper for aiobotocore S3 2.20.1 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore S3 client
    async with session.s3.create_client() as s3_client:
        s3_client: types_aiobotocore_s3.client.S3Client```
"""

from __future__ import annotations

from types_aiobotocore_s3.client import S3Client
from types_aiobotocore_s3.paginator import (
    ListBucketsPaginator,
    ListDirectoryBucketsPaginator,
    ListMultipartUploadsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListObjectVersionsPaginator,
    ListPartsPaginator,
)
from types_aiobotocore_s3.waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)

from boto34.aiobotocore.client_factory import ClientFactory
from boto34.aiobotocore.service_factory import ServiceFactory


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
    ServiceFactory[
        S3Client,
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
