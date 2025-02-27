"""
Wrapper for aioboto3 LicenseManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_license_manager/)

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
    # Returns type annotated aioboto3 LicenseManager client
    license_manager_client = session.license_manager.client()
    license_manager_client: types_aiobotocore_license_manager.client.LicenseManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_license_manager.client import LicenseManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class LicenseManagerService(ServiceFactory[LicenseManagerClient]):
    SERVICE_NAME = "license-manager"
    _SERVICE_PROP = "license_manager"
