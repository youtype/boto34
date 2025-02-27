"""
Wrapper for aioboto3 CloudHSMV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudhsmv2/)

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
    # Returns type annotated aioboto3 CloudHSMV2 client
    cloudhsmv2_client = session.cloudhsmv2.client()
    cloudhsmv2_client: types_aiobotocore_cloudhsmv2.client.CloudHSMV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudhsmv2.client import CloudHSMV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class CloudHSMV2Service(ServiceFactory[CloudHSMV2Client]):
    SERVICE_NAME = "cloudhsmv2"
    _SERVICE_PROP = "cloudhsmv2"
