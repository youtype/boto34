"""
Wrapper for boto3 OpsWorks service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opsworks/)

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
    # Returns type annotated boto3 OpsWorks client
    opsworks_client = session.opsworks.client()
    opsworks_client: types_boto3_opsworks.client.OpsWorksClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 OpsWorks resource
    opsworks_resource = session.opsworks.resource()
    opsworks_resource: types_boto3_opsworks.service_resource.OpsWorksServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_opsworks.client import OpsWorksClient
from types_boto3_opsworks.service_resource import OpsWorksServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class OpsWorksService(ServiceResourceFactory[OpsWorksClient, OpsWorksServiceResource]):
    SERVICE_NAME = "opsworks"
    _SERVICE_PROP = "opsworks"
