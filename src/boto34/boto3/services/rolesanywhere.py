"""
Wrapper for boto3 IAMRolesAnywhere service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rolesanywhere/)

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
    # Returns type annotated boto3 IAMRolesAnywhere client
    rolesanywhere_client = session.rolesanywhere.client()
    rolesanywhere_client: types_boto3_rolesanywhere.client.IAMRolesAnywhereClient
    ```
"""

from __future__ import annotations

from types_boto3_rolesanywhere.client import IAMRolesAnywhereClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_rolesanywhere.client import IAMRolesAnywhereClient
except ImportError:
    IAMRolesAnywhereClient = object  # type: ignore[misc,assignment]


class IAMRolesAnywhereService(
    ServiceFactory[IAMRolesAnywhereClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rolesanywhere"
    _SERVICE_PROP = "rolesanywhere"
