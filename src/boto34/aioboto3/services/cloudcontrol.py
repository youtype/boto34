"""
Wrapper for aioboto3 CloudControlApi service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudcontrol/)

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
    # Returns type annotated aioboto3 CloudControlApi client
    cloudcontrol_client = session.cloudcontrol.client()
    cloudcontrol_client: types_aiobotocore_cloudcontrol.client.CloudControlApiClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudcontrol.client import CloudControlApiClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudControlApiService(ServiceFactory[CloudControlApiClient]):
    SERVICE_NAME = "cloudcontrol"
    _SERVICE_PROP = "cloudcontrol"
