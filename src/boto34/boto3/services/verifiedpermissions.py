"""
Wrapper for boto3 VerifiedPermissions service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_verifiedpermissions/)

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
    # Returns type annotated boto3 VerifiedPermissions client
    verifiedpermissions_client = session.verifiedpermissions.client()
    verifiedpermissions_client: types_boto3_verifiedpermissions.client.VerifiedPermissionsClient
    ```
"""

from __future__ import annotations

from types_boto3_verifiedpermissions.client import VerifiedPermissionsClient

from boto34.boto3.service_factory import ServiceFactory


class VerifiedPermissionsService(ServiceFactory[VerifiedPermissionsClient]):
    SERVICE_NAME = "verifiedpermissions"
    _SERVICE_PROP = "verifiedpermissions"
