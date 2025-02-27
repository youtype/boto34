"""
Wrapper for aioboto3 OpsWorks service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opsworks/)

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
    # Returns type annotated aioboto3 OpsWorks client
    opsworks_client = session.opsworks.client()
    opsworks_client: types_aiobotocore_opsworks.client.OpsWorksClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 OpsWorks resource
    opsworks_resource = session.opsworks.resource()
    opsworks_resource: types_aiobotocore_opsworks.service_resource.OpsWorksServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_opsworks.client import OpsWorksClient
from types_aiobotocore_opsworks.service_resource import OpsWorksServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class OpsWorksService(ServiceResourceFactory[OpsWorksClient, OpsWorksServiceResource]):
    SERVICE_NAME = "opsworks"
    _SERVICE_PROP = "opsworks"
