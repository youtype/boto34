"""
Wrapper for aioboto3 IAM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iam/)

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
    # Returns type annotated aioboto3 IAM client
    iam_client = session.iam.client()
    iam_client: types_aiobotocore_iam.client.IAMClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 IAM resource
    iam_resource = session.iam.resource()
    iam_resource: types_aiobotocore_iam.service_resource.IAMServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_iam.client import IAMClient
from types_aiobotocore_iam.service_resource import IAMServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class IAMService(ServiceResourceFactory[IAMClient, IAMServiceResource]):
    SERVICE_NAME = "iam"
    _SERVICE_PROP = "iam"
