"""
Wrapper for aioboto3 Glacier service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_glacier/)

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
    # Returns type annotated aioboto3 Glacier client
    glacier_client = session.glacier.client()
    glacier_client: types_aiobotocore_glacier.client.GlacierClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 Glacier resource
    glacier_resource = session.glacier.resource()
    glacier_resource: types_aiobotocore_glacier.service_resource.GlacierServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_glacier.client import GlacierClient
from types_aiobotocore_glacier.service_resource import GlacierServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class GlacierService(ServiceResourceFactory[GlacierClient, GlacierServiceResource]):
    SERVICE_NAME = "glacier"
    _SERVICE_PROP = "glacier"
