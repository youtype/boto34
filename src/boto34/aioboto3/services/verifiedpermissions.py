"""
Wrapper for aioboto3 VerifiedPermissions service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_verifiedpermissions/)

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
    # Returns type annotated aioboto3 VerifiedPermissions client
    verifiedpermissions_client = session.verifiedpermissions.client()
    verifiedpermissions_client: types_aiobotocore_verifiedpermissions.client.VerifiedPermissionsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient

from boto34.aioboto3.service_factory import ServiceFactory


class VerifiedPermissionsService(ServiceFactory[VerifiedPermissionsClient]):
    SERVICE_NAME = "verifiedpermissions"
    _SERVICE_PROP = "verifiedpermissions"
